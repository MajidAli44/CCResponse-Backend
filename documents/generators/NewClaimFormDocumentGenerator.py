from documents.generators import AbstractDocumentGenerator
from documents.serializers import NewClaimFormDocumentSerializer


class NewClaimFormDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'New Claim Form.docx'

    def fields(self):
        return [
            'client_name', 'client_phone_number', 'client_email_address', 'client_date_of_birth', 'client_address',
            'client_vrn', 'client_vehicle_model', 'client_vehicle_make', 'accident_date', 'approx_location',
            'approx_circumstances', 'approx_other_info', 'tp_name', 'tp_address', 'tp_vrn', 'tp_vehicle_make',
            'tp_vehicle_model', 'client_mot_expiry', 'client_tax_expiry', 'client_insurer_name', 'approx_time',
            'tp_mot_expiry', 'tp_tax_expiry', 'tp_insurer', 'tp_policy_number', 'tp_insurer_phone_number',
            'tp_insurer_email', 'tp_insurer_ref', 'tp_other_details', 'client_ni_number', 'client_extra',
            'client_d_licence', 'tp_phone_number',
        ]

    def document_serializer(self):
        return NewClaimFormDocumentSerializer

    def is_docx_template(self):
        return True

    def is_pdf_file(self):
        return False
