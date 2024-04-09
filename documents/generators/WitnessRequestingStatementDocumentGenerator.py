from documents.generators import AbstractDocumentGenerator
from documents.serializers import WitnessRequestingStatementDocumentSerializer


class WitnessRequestingStatementDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'Letter to Witness Requesting Statement.docx'

    def fields(self):
        return ['client_name', 'client_vrn', 'accident_date']

    def document_serializer(self):
        return WitnessRequestingStatementDocumentSerializer

    def is_docx_template(self):
        return True

    def is_pdf_file(self):
        return False
