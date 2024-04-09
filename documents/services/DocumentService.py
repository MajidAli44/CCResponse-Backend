import zipfile
from io import BytesIO

from common.services.StorageService import storageService
from documents.models import Document, DocumentTemplates
from documents.services import DocumentTypes


class DocumentService:

    @staticmethod
    def generate_document_templates(case_id: int):
        for current_document in DocumentTypes.DOCUMENT_FIELDS:
            document = DocumentTypes.DOCUMENT_FIELDS[current_document]
            if 'generator' in document:
                generator = document['generator'](case_id)
                not_filled_fields = generator.generate_not_filled_fields()

                existed_document = DocumentTemplates.objects.filter(case_id=case_id, template_name=current_document, empty_fields=not_filled_fields)
                if len(existed_document) == 1:
                    continue

                DocumentTemplates.objects.filter(case_id=case_id, template_name=current_document).delete()
                DocumentTemplates.objects.create(
                    case_id=case_id, name=current_document, empty_fields=not_filled_fields,
                    document_need_sign=document['is_to_sign'], template_name=current_document,
                )

    @staticmethod
    def generate_document(case_id: int, template_name: str):
        document_info = DocumentTypes.DOCUMENT_FIELDS[template_name]
        generator = document_info['generator'](case_id)
        not_filled_fields, file_bytes = generator.generate()
        rel_file_path = storageService.put_into_s3_from_stream(file_bytes, f'documents/{case_id}',
                                                               generator.document_name())

        return Document.objects.create(
            case_id=case_id, name=template_name, rel_file_path=rel_file_path,
            empty_fields=not_filled_fields, auto_generated_document=True, display_document_in_table=True,
            document_need_sign=document_info['is_to_sign']
        )

    @staticmethod
    def get_files_zip_url(files):
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED, False) as zip_file:
            for document_file in files:
                real_file_name = document_file.rel_file_path.split('/')
                real_file_name = real_file_name[len(real_file_name) - 1]
                zip_file.writestr(real_file_name, storageService.get_from_s3_to_bytes(document_file.rel_file_path))
        zip_buffer.seek(0)
        s3_zip_obj = storageService.put_into_s3_from_stream(file_stream=zip_buffer,
                                                            folder='case_documents/',
                                                            file_name='Documents.zip')
        return storageService.get_s3_presigned_url(s3_zip_obj)

    @classmethod
    def get_document_url(cls, document_ids):
        documents = Document.objects.filter(id__in=document_ids)
        if documents.count() == 1:
            return storageService.get_s3_presigned_url(documents.first().rel_file_path)
        document_files = [document for document in documents]
        return cls.get_files_zip_url(document_files)