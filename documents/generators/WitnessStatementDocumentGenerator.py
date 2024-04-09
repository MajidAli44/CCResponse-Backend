from documents.generators import AbstractDocumentGenerator
from documents.serializers import WitnessStatementDocumentSerializer


class WitnessStatementDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'Witness Statement.pdf'

    def fields(self):
        return []

    def document_serializer(self):
        return WitnessStatementDocumentSerializer

    def is_docx_template(self):
        return False

    def is_pdf_file(self):
        return True