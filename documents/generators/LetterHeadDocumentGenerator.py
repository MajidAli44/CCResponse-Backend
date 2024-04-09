from documents.generators import AbstractDocumentGenerator
from documents.serializers import LetterHeadDocumentSerializer


class LetterHeadDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'Letter Head.docx'

    def fields(self):
        return []

    def document_serializer(self):
        return LetterHeadDocumentSerializer

    def is_docx_template(self):
        return True

    def is_pdf_file(self):
        return False
