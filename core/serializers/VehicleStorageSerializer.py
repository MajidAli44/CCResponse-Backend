from rest_framework import serializers

from core.models import VehicleStorage
from .VehicleActionSerializer import VehicleActionSerializer


class VehicleStorageSerializer(VehicleActionSerializer):
    days_in_storage = serializers.SerializerMethodField()

    class Meta:
        model = VehicleStorage
        fields = '__all__'

    def get_days_in_storage(self, obj: VehicleStorage):
        return (obj.end_date - obj.start_date).days if obj.end_date else None
