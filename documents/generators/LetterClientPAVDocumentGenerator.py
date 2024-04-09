from documents.generators import AbstractDocumentGenerator
from documents.serializers import LetterClientPAVDocumentSerializer


class LetterClientPAVDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'Letter to Client with PAV.docx'

    def fields(self):
        return ['client_name', 'client_vrn', 'accident_date', 'client_insurer']

    def document_serializer(self):
        return LetterClientPAVDocumentSerializer

    def is_docx_template(self):
        return True

    def is_pdf_file(self):
        return False
