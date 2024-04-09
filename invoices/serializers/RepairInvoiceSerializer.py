from decimal import Decimal

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from invoices.models import RepairInvoice
from invoices.serializers import RepairInvoiceItemSerializer


class RepairInvoiceSerializer(WritableNestedModelSerializer):
    items = RepairInvoiceItemSerializer(allow_null=True, required=False, many=True)
    labour_total = serializers.SerializerMethodField()
    total_repair_fee = serializers.SerializerMethodField()
    repair_invoice_total = serializers.FloatField(read_only=True, allow_null=True)

    class Meta:
        model = RepairInvoice
        fields = (
            'labour_hours', 'labour_rate', 'labour_total', 'items',
            'paint_and_sundries', 'parts_mlp', 'remove_and_refit_glass',
            'covid_clean_and_ppe', 'specialist_1', 'miscellaneous_1',
            'car_kit_and_mini_valet', 'geometry', 'anti_corrosion',
            'epa', 'total_repair_fee', 'repair_invoice_total'
        )
        read_only_fields = ('labour_total',)

    def get_labour_total(self, obj):
        if obj.labour_hours is None or obj.labour_rate is None:
            return None

        labour_hours = Decimal(obj.labour_hours)
        labour_rate = Decimal(obj.labour_rate)
        return (labour_hours * labour_rate).quantize(Decimal('0.00'))

    def get_total_repair_fee(self, obj):
        total = Decimal('0.0')
        item_total = Decimal('0.0')
        for item in obj.items.all():
            item_total += item.price
        total += (item_total + obj.repair_invoice_total).quantize(Decimal('0.0'))
        return total
