from drf_writable_nested import WritableNestedModelSerializer

from cases.models import Case
from invoices.serializers import RepairInvoiceSerializer
from parties.serializers import ClientSerializer, ThirdPartySerializer
from .CaseCreatorDetailsSerializer import CaseCreatorSerializer
from .FileHandlerSerializer import FileHandlerSerializer
from .HireValidationSerializer import HireValidationSerializer
from .AccidentSerializer import AccidentSerializer
from .ClawbackDetailSerializer import ClawbackDetailSerializer
from .HireDetailSerializer import HireDetailSerializer
from .PIDetailSerializer import PIDetailSerializer
from .RecoveryDetailSerializer import RecoveryDetailSerializer
from .StorageDetailSerializer import StorageDetailSerializer
from .HireAgreementSerializer import HireAgreementSerializer
from .CaseFeeSerializer import CaseFeeSerializer


class CaseUpdateSerializer(WritableNestedModelSerializer):
    """ Serializer for case update """
    client = ClientSerializer(allow_null=True, required=False)
    third_party = ThirdPartySerializer(allow_null=True, required=False)
    accident = AccidentSerializer(allow_null=True, required=False)
    hire_detail = HireDetailSerializer(allow_null=True, required=False)
    hire_validation = HireValidationSerializer(allow_null=True, required=False)
    hire_agreement = HireAgreementSerializer(allow_null=True, required=False)
    storage_detail = StorageDetailSerializer(allow_null=True, required=False)
    pi_detail = PIDetailSerializer(allow_null=True, required=False)
    recovery_detail = RecoveryDetailSerializer(allow_null=True, required=False)
    clawback_detail = ClawbackDetailSerializer(allow_null=True, required=False)
    case_fee = CaseFeeSerializer(allow_null=True, required=False)
    repair_invoice = RepairInvoiceSerializer(allow_null=True, required=False)
    case_creator = CaseCreatorSerializer(allow_null=True, required=True)
    file_handler = FileHandlerSerializer(allow_null=True, required=True)

    class Meta:
        model = Case
        fields = (
            'id', 'services', 'cc_ref', 'case_creator', 'file_handler', 'instruction_date', 'client', 'accident', 'third_party',
            'solicitor', 'payment_status', 'solicitor_ref', 'provider',
            'retained_date', 'introducer', 'introducer_fee', 'hire_detail',
            'hire_validation', 'hire_agreement', 'storage_detail', 'pi_detail', 'recovery_detail',
            'clawback_detail', 'status', 'status_description', 'case_fee', 'case_source', 'repair_invoice',
            'recovery_agent'
        )

    def validate(self, attrs):
        if 'status' in attrs:
            status = attrs['status']
            if 'status_description' not in attrs:
                if status == Case.CaseStatuses.lead:
                    attrs['status_description'] = Case.CaseStatusDescription.lead_new_lead
                elif status == Case.CaseStatuses.ongoing:
                    attrs['status_description'] = Case.CaseStatusDescription.ongoing_accepted
                elif status == Case.CaseStatuses.payment_pack:
                    attrs['status_description'] = Case.CaseStatusDescription.payment_pack_pp_issued
                elif status in [Case.CaseStatuses.settled, Case.CaseStatuses.closed]:
                    attrs['status_description'] = Case.CaseStatusDescription.settled_closed_no_contact
            else:
                available_statuses = Case.get_available_status_descriptions()
                for current_available_status in available_statuses:
                    if current_available_status['status'] != status:
                        continue

                    if attrs['status_description'] not in current_available_status['accepted_descriptions']:
                        attrs['status_description'] = current_available_status['default']
        return attrs

