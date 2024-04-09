from documents.generators import AbstractDocumentGenerator
from documents.serializers import NoticeRightCancelDocumentSerializer


class NoticeRightCancelDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'Notice of Right to Cancel.docx'

    def fields(self):
        return ['current_date', 'client_name', 'client_address']

    def document_serializer(self):
        return NoticeRightCancelDocumentSerializer

    def is_docx_template(self):
        return True

    def is_pdf_file(self):
        return False
