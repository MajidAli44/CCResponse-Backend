from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from cases.models import Case
from invoices.serializers import RepairInvoiceSerializer
from parties.serializers import ClientSerializer, ThirdPartySerializer, ProviderSerializer
from .AccidentSerializer import AccidentSerializer
from .CaseCreatorDetailsSerializer import CaseCreatorSerializer
from .CaseFeeSerializer import CaseFeeSerializer
from .ClawbackDetailSerializer import ClawbackDetailSerializer
from .FileHandlerSerializer import FileHandlerSerializer
from .HireAgreementSerializer import HireAgreementSerializer
from .HireDetailSerializer import HireDetailSerializer
from .HireValidationSerializer import HireValidationSerializer
from .PIDetailSerializer import PIDetailSerializer
from .RecoveryDetailSerializer import RecoveryDetailSerializer
from .StorageDetailSerializer import StorageDetailSerializer


class CaseDetailSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    client = ClientSerializer(allow_null=True, required=False)
    third_party = ThirdPartySerializer(allow_null=True, required=False)
    accident = AccidentSerializer(allow_null=True, required=False)
    hire_detail = HireDetailSerializer(allow_null=True, required=False)
    hire_validation = HireValidationSerializer(allow_null=True, required=False)
    hire_agreement = HireAgreementSerializer(required=False, allow_null=True)
    storage_detail = StorageDetailSerializer(allow_null=True, required=False)
    pi_detail = PIDetailSerializer(allow_null=True, required=False)
    recovery_detail = RecoveryDetailSerializer(allow_null=True, required=False)
    clawback_detail = ClawbackDetailSerializer(allow_null=True, required=False)
    provider = ProviderSerializer(allow_null=True, required=False)
    case_fee = CaseFeeSerializer(allow_null=True, required=False)
    repair_invoice = RepairInvoiceSerializer(allow_null=True, required=False)
    case_creator = CaseCreatorSerializer(allow_null=True, required=True)
    file_handler = FileHandlerSerializer(allow_null=True, required=True)
    case_price = serializers.ReadOnlyField(source="case_value", read_only=True)
    case_selections = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Case
        fields = (
            'id', 'case_price', 'case_selections', 'services', 'service_providers', 'cc_ref', 'case_creator',
            'file_handler',
            'instruction_date', 'client', 'accident', 'third_party',
            'solicitor', 'payment_status', 'solicitor_ref', 'provider',
            'retained_date', 'introducer', 'introducer_fee',
            'hire_detail', 'hire_validation', 'hire_agreement', 'storage_detail',
            'pi_detail', 'recovery_detail', 'clawback_detail', 'status', 'status_description',
            'case_fee', 'case_source', 'repair_invoice', 'recovery_agent'
        )

    def get_case_selections(self, obj):
        hire_detail = False
        vd_repairable = False

        if obj.hire_detail.vehicle is not None or obj.hire_detail.start_date is not None or obj.hire_detail.end_date is not None:
            hire_detail = True

        if obj.hire_validation.repairable:
            vd_repairable = True

        data = {
            'hire_detail': hire_detail,
            'vd_repairable': vd_repairable

        }
        return data