from rest_framework import serializers

from invoices.models import RepairInvoiceItem


class RepairInvoiceItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = RepairInvoiceItem
        fields = ('name', 'price')
