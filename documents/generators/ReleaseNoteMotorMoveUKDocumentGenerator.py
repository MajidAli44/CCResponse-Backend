from documents.generators import AbstractDocumentGenerator
from documents.serializers import ReleaseNoteMotorMoveUKDocumentSerializer


class ReleaseNoteMotorMoveUKDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'Release Note Motor Move UK.docx'

    def fields(self):
        return ['client_name', 'client_vrn', 'client_vehicle_model', 'client_vehicle_make', 'accident_date', 'client_address']

    def document_serializer(self):
        return ReleaseNoteMotorMoveUKDocumentSerializer

    def is_docx_template(self):
        return True

    def is_pdf_file(self):
        return False
