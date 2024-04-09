from rest_framework import serializers

from invoices.models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    total_net = serializers.DecimalField(decimal_places=2, max_digits=12, required=False, allow_null=True)
    total_vat = serializers.DecimalField(decimal_places=2, max_digits=12, required=False, allow_null=True)
    total = serializers.DecimalField(decimal_places=2, max_digits=12, required=False, allow_null=True)

    class Meta:
        model = Invoice
        fields = (
            'id', 'case', 'charge_type', 'total_net', 'total_vat', 'total', 'settlement_fee'
        )
        read_only_fields = (
            'id', 'case', 'charge_type', 'total_net', 'total_vat', 'total'
        )
