from datetime import date

from rest_framework import serializers

from cases.models import Case


class RepairInvoiceDocumentSerializer(serializers.ModelSerializer):

    current_date = serializers.SerializerMethodField()
    client_cc_ref = serializers.CharField(source='cc_ref')
    client_vrn = serializers.CharField(source='client.vehicle.vrn', allow_null=True)
    client_name = serializers.CharField(source='client.name', allow_null=True)
    accident_date = serializers.DateField(source='accident.accident_date', allow_null=True)
    tp_name = serializers.CharField(source='third_party.name', allow_null=True)
    tp_insurer_ref = serializers.CharField(source='third_party.insurer_ref', allow_null=True)

    class Meta:
        model = Case
        fields = (
            'current_date', 'client_cc_ref', 'client_name', 'accident_date', 'tp_name', 'tp_insurer_ref', 'client_vrn'
        )

    def get_current_date(self, _):
        return date.today().strftime("%d/%m/%Y")
