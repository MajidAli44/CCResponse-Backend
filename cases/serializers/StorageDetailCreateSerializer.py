from rest_framework import serializers

from cases.models import StorageDetail


class StorageDetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageDetail
        fields = ('provider', 'status', 'provider_ref', 'from_date', 'fee_per_day', 'engineers_fee',)
