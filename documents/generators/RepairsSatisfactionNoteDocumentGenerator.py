from documents.generators import AbstractDocumentGenerator
from documents.serializers import RepairsSatisfactionNoteDocumentSerializer


class RepairsSatisfactionNoteDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'Client Vehicle Repairs Satisfaction Note.docx'

    def fields(self):
        return [
            'current_date', 'client_name', 'client_vrn', 'client_vehicle_model', 'client_vehicle_make',
            'accident_date', 'client_address'
        ]

    def document_serializer(self):
        return RepairsSatisfactionNoteDocumentSerializer

    def is_docx_template(self):
        return True

    def is_pdf_file(self):
        return False