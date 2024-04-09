from documents.generators import AbstractDocumentGenerator
from documents.serializers import StatementOfTruthDocumentSerializer


class StatementOfTruthDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'Statement of Truth.docx'

    def fields(self):
        return []

    def document_serializer(self):
        return StatementOfTruthDocumentSerializer

    def is_docx_template(self):
        return True

    def is_pdf_file(self):
        return False
