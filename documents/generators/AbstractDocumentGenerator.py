import os
from abc import ABC, abstractmethod
from decimal import Decimal
from io import BytesIO

from docxtpl import DocxTemplate

from cases.models import Case
from ccresponse.settings import BASE_DIR


class AbstractDocumentGenerator(ABC):

    def __init__(self, case_id):
        self.__case = Case.objects.get(id=case_id)

    @abstractmethod
    def document_name(self):
        return NotImplementedError()

    @abstractmethod
    def fields(self):
        raise NotImplementedError()

    @abstractmethod
    def document_serializer(self):
        raise NotImplementedError()

    @abstractmethod
    def is_docx_template(self):
        raise NotImplementedError()

    @abstractmethod
    def is_pdf_file(self):
        raise NotImplementedError()

    def get_template_path(self):
        return os.path.join(BASE_DIR, 'documents', 'document_templates', self.document_name())

    def generate(self):
        if self.is_docx_template():
            return self.generate_docx_template()

        if self.is_pdf_file():
            return self.generate_pdf_file()

        raise NotImplementedError('Not implemented file type, see fields is_docx_template and is_pdf_file')

    def generate_not_filled_fields(self):
        if self.is_pdf_file():
            return []

        filled_fields = self.document_serializer()(self.__case).data

        not_filled_fields = []

        for key in self.fields():
            if key not in filled_fields:
                not_filled_fields.append(key)
            elif filled_fields[key] in [None, '']:
                not_filled_fields.append(key)

        return not_filled_fields

    def generate_docx_template(self):
        template_path = self.get_template_path()
        filled_fields = self.document_serializer()(self.__case).data

        not_filled_fields = []
        template_data = {}

        for key in self.fields():
            if key not in filled_fields:
                not_filled_fields.append(key)

        for key, value in filled_fields.items():
            if value is None and key in self.fields():
                if key not in not_filled_fields:
                    not_filled_fields.append(key)
                template_data[key] = ''
                continue
            template_data[key] = AbstractDocumentGenerator.prepare_value(value)
            if type(value) == bool:
                k, v = AbstractDocumentGenerator.prepare_bool(key, value)
                template_data[k] = v

        template_data = self.process_fields_before_render(fields=template_data)

        template = DocxTemplate(template_path)
        template.render(template_data)

        file_bytes = BytesIO()
        template.save(file_bytes)
        file_bytes.seek(0)

        return not_filled_fields, file_bytes

    def process_fields_before_render(self, fields: dict):
        return fields

    @staticmethod
    def prepare_value(value):
        if type(value) in [Decimal, int]:
            return f'{value:,}'
        elif type(value) == str:
            return value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        return value
    
    @staticmethod
    def prepare_bool(key, value):
        if value:
            return f'{key}_yes', '✓'
        else:
            return f'{key}_no', '✓'

    def generate_pdf_file(self):
        template_path = self.get_template_path()

        file_bytes = BytesIO()
        with open(template_path, 'rb') as file:
            file_bytes.write(file.read())
        file_bytes.seek(0)

        return [], file_bytes

    def get_case(self):
        return self.__case