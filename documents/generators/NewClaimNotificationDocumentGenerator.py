from documents.generators import AbstractDocumentGenerator
from documents.serializers import NewClaimNotificationDocumentSerializer


class NewClaimNotificationDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'New Claim Notification.docx'

    def fields(self):
        return [
            'current_date', 'client_cc_ref', 'client_name', 'client_vrn', 'accident_date', 'tp_name', 'tp_vrn',
            'tp_insurer_ref', 'hire_fee_per_day', 'recovery_fee', 'storage_fee_per_day', 'engineer_fee',
            'tp_policy_number'
        ]

    def document_serializer(self):
        return NewClaimNotificationDocumentSerializer

    def is_docx_template(self):
        return True

    def is_pdf_file(self):
        return False
