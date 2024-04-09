from documents.generators import AbstractDocumentGenerator
from documents.serializers import HirePackDocumentSerializer


class HirePackDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'Client Hire Document Pack and Care Letters.docx'

    def fields(self):
        return [
            'current_date', 'client_cc_ref', 'client_name', 'tp_insurer_ref', 'tp_name',
            'accident_date', 'client_vrn', 'client_address', 'client_phone_number',
            'client_vehicle_make_model', 'storage_from', 'storage_to', 'storage_fee_per_day', 'days_in_storage',
            'recovery_amount', 'total_storage_amount', 'client_date_of_birth', 'client_license_number',
            'hire_mk_md', 'hire_vrn', 'hire_start_date', 'hire_end_date',
            'hire_charge_per_day', 'cdw_per_day', 'tmdr', 'tmdrc', 'driver_name', 'driver_license_number',
            'driver_dob', 'hire_due_back_date', 'prosecution', 'accident_loss_in_3_past_years',
            'proposal_declined_or_increased_fees', 'diseases', 'offer_received', 'extras_total',
            'nsi_age', 'nsi_occupation', 'nsi_driving_licence', 'nsi_convictions_points',
        ]

    def document_serializer(self):
        return HirePackDocumentSerializer

    def is_docx_template(self):
        return True

    def is_pdf_file(self):
        return False
