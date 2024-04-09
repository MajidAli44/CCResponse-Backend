from rest_framework import serializers

from core.models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = (
            'id',
            'invoice_number', 'invoice_date', 'date_paid',
            'invoice_type', 'settlement_status',
            'total_net', 'total_vat',
            'settled_amount_net', 'settled_amount_vat', 'settled_amount_total',
            'total'
        )

    def get_total(self, obj):
        v = (obj.total_net or 0) + (obj.total_vat or 0)
        return v and ("%.2f" % v) or None
