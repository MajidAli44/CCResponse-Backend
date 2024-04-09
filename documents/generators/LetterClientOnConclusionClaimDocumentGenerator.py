from documents.generators import AbstractDocumentGenerator
from documents.serializers import LetterClientOnConclusionClaimDocumentSerializer


class LetterClientOnConclusionClaimDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'Letter to Client on Conclusion of Claim.docx'

    def fields(self):
        return ['client_name', 'client_vrn', 'accident_date', 'client_insurer']

    def document_serializer(self):
        return LetterClientOnConclusionClaimDocumentSerializer

    def is_docx_template(self):
        return True

    def is_pdf_file(self):
        return False
