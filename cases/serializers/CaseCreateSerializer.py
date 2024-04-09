from datetime import date

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from cases.models import Case
from invoices.serializers import RepairInvoiceSerializer
from parties.serializers import ClientSerializer, ThirdPartySerializer

from .AccidentSerializer import AccidentSerializer
from .HireDetailSerializer import HireDetailSerializer
from .StorageDetailCreateSerializer import StorageDetailCreateSerializer
from .PIDetailSerializer import PIDetailSerializer
from .RecoveryDetailSerializer import RecoveryDetailSerializer
from .ClawbackDetailSerializer import ClawbackDetailSerializer
from .HireValidationSerializer import HireValidationSerializer
from .HireAgreementSerializer import HireAgreementSerializer
from .CaseFeeSerializer import CaseFeeSerializer


class CaseCreateSerializer(WritableNestedModelSerializer):
    instruction_date = serializers.DateField(required=False, allow_null=True)
    client = ClientSerializer(required=False, allow_null=True)
    third_party = ThirdPartySerializer(required=False, allow_null=True)
    accident = AccidentSerializer(required=False, allow_null=True)
    hire_detail = HireDetailSerializer(required=False, allow_null=True)
    hire_validation = HireValidationSerializer(required=False, allow_null=True)
    hire_agreement = HireAgreementSerializer(required=False, allow_null=True)
    storage_detail = StorageDetailCreateSerializer(required=False, allow_null=True)
    pi_detail = PIDetailSerializer(required=False, allow_null=True)
    recovery_detail = RecoveryDetailSerializer(required=False, allow_null=True)
    clawback_detail = ClawbackDetailSerializer(required=False, allow_null=True)
    case_fee = CaseFeeSerializer(allow_null=True, required=False)
    repair_invoice = RepairInvoiceSerializer(allow_null=True, required=False)

    class Meta:
        model = Case
        fields = (
            'id', 'services', 'cc_ref', 'file_handler', 'instruction_date', 'client', 'accident', 'third_party',
            'solicitor', 'solicitor_ref', 'payment_status', 'retained_date',
            'introducer', 'introducer_fee', 'provider', 'hire_detail',
            'hire_validation', 'hire_agreement', 'storage_detail', 'pi_detail', 'recovery_detail',
            'clawback_detail', 'case_fee', 'case_source', 'repair_invoice', 'recovery_agent'
        )

    def validate_instruction_date(self, value):
        return value or date.today()
