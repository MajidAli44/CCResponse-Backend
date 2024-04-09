from rest_framework import serializers

from invoices.models import InvoiceFile


class InvoicesListSerializer(serializers.ModelSerializer):

    date_created = serializers.DateField(source='last_invoice_date', allow_null=True)
    client_name = serializers.CharField(source='case.client.name', allow_null=True, allow_blank=True)
    file_ref = serializers.CharField(source='case.cc_ref', allow_null=True, allow_blank=True)
    settlement_status = serializers.CharField(source='case.status_description', allow_null=True, allow_blank=True)
    recovery_agent = serializers.CharField(source='case.recovery_agent', allow_null=True, allow_blank=True)
    number_of_invoices = serializers.IntegerField(source='invoice_count', allow_null=True)
    total = serializers.DecimalField(allow_null=True, decimal_places=2, max_digits=12)

    class Meta:
        model = InvoiceFile
        fields = (
            'pk', 'date_created', 'client_name', 'file_ref',
            'recovery_agent', 'settlement_status', 'number_of_invoices',
            'total'
        )
