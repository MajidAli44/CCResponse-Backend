from decimal import Decimal

from rest_framework import serializers

from cases.models import CaseFee


class CaseFeeSerializer(serializers.ModelSerializer):

    total = serializers.SerializerMethodField()
    profit = serializers.SerializerMethodField()

    class Meta:
        model = CaseFee
        fields = (
            'outsourced_to', 'repair_status', 'hire_ref_fee', 'repair_ref_fee', 'total',
            'salvage_value', 'sold_via', 'sale_price', 'profit'
        )
        read_only_fields = ('total', 'profit')

    def get_profit(self, obj):
        if obj.sale_price is not None and obj.salvage_value is not None:
            sale_price = Decimal(obj.sale_price)
            salvage_value = Decimal(obj.salvage_value)
            return sale_price - salvage_value
        return None

    def get_total(self, obj):
        if obj.hire_ref_fee is None or obj.repair_ref_fee is None or obj.sale_price is None or obj.salvage_value is None:
            return None

        hire_ref_fee = obj.hire_ref_fee
        repair_ref_fee = Decimal(obj.repair_ref_fee)
        sale_price = Decimal(obj.sale_price)
        salvage_value = Decimal(obj.salvage_value)

        if hire_ref_fee == CaseFee.HireRefFee.fee_na:
            hire_ref_fee = Decimal(0.0)
        elif hire_ref_fee == CaseFee.HireRefFee.fee_450:
            hire_ref_fee = Decimal(450.0)
        elif hire_ref_fee == CaseFee.HireRefFee.fee_500:
            hire_ref_fee = Decimal(500.0)
        elif hire_ref_fee == CaseFee.HireRefFee.fee_750:
            hire_ref_fee = Decimal(750.0)

        total = Decimal(0)
        total += hire_ref_fee
        total += repair_ref_fee
        total += sale_price - salvage_value

        return total
