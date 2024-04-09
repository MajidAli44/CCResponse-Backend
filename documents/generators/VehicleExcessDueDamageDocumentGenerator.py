from documents.generators import AbstractDocumentGenerator
from documents.serializers import VehicleExcessDueDamageDocumentSerializer


class VehicleExcessDueDamageDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'Letter to Client Vehicle Excess Due to Damage.docx'

    def fields(self):
        return ['client_name', 'client_vrn', 'accident_date', 'client_address']

    def document_serializer(self):
        return VehicleExcessDueDamageDocumentSerializer

    def is_docx_template(self):
        return True

    def is_pdf_file(self):
        return False
