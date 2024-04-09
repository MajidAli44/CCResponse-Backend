from datetime import date

from rest_framework import serializers

from cases.models import Case


class NewClaimNotificationDocumentSerializer(serializers.ModelSerializer):

    current_date = serializers.SerializerMethodField()
    client_cc_ref = serializers.CharField(source='cc_ref')
    client_name = serializers.CharField(source='client.name', allow_null=True)
    client_vrn = serializers.CharField(source='client.vehicle.vrn', allow_null=True)
    accident_date = serializers.DateField(source='accident.accident_date', allow_null=True)
    tp_name = serializers.CharField(source='third_party.name', allow_null=True)
    tp_vrn = serializers.CharField(source='third_party.vehicle.vrn', allow_null=True)
    tp_insurer_ref = serializers.CharField(source='third_party.insurer_ref', allow_null=True)
    tp_policy_number = serializers.SerializerMethodField()

    hire_fee_per_day = serializers.DecimalField(source='hire_detail.hire_fee_per_day', decimal_places=2, max_digits=12, default=0)
    recovery_fee = serializers.DecimalField(source='recovery_detail.recovery_fee', decimal_places=2, max_digits=12, default=0)
    storage_fee_per_day = serializers.DecimalField(source='storage_detail.fee_per_day', decimal_places=2, max_digits=12, default=0)
    engineer_fee = serializers.DecimalField(source='storage_detail.engineers_fee', decimal_places=2, max_digits=12, default=0)

    class Meta:
        model = Case
        fields = (
            'current_date', 'client_cc_ref', 'client_name', 'client_vrn', 'accident_date', 'tp_name', 'tp_vrn',
            'tp_insurer_ref', 'hire_fee_per_day', 'recovery_fee', 'storage_fee_per_day', 'engineer_fee',
            'tp_policy_number'
        )

    def get_current_date(self, _):
        return date.today().strftime("%d/%m/%Y")

    def get_tp_policy_number(self, obj):
        if obj.third_party:
            if obj.third_party.policy_number:
                return obj.third_party.policy_number
        return "TBC"

