from rest_framework import serializers

from cases.models import StorageDetail


class StorageDetailSerializer(serializers.ModelSerializer):
    days_in_storage = serializers.IntegerField(read_only=True, default=0)
    storage_total_fee = serializers.FloatField(source="get_storage_total_fee", read_only=True, default=0)

    class Meta:
        model = StorageDetail
        fields = (
            'provider', 'status', 'provider_ref', 'from_date', 'end_date', 'fee_per_day', 'engineers_fee',
            'days_in_storage', 'storage_total_fee'
        )
