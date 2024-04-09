from documents.generators import AbstractDocumentGenerator
from documents.serializers import ReleaseNoteMansfieldGroupDocumentSerializer


class ReleaseNoteMansfieldGroupDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'Release Note Mansfield Group.docx'

    def fields(self):
        return [
            'client_name', 'client_vrn', 'client_vehicle_model', 'client_vehicle_make', 'accident_date', 'client_address'
        ]

    def document_serializer(self):
        return ReleaseNoteMansfieldGroupDocumentSerializer

    def is_docx_template(self):
        return True

    def is_pdf_file(self):
        return False
