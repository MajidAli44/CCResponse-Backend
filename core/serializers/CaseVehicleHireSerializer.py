from rest_framework import serializers

from core.models import Vehicle, VehicleHire
from .VehicleActionSerializer import VehicleActionSerializer


class CaseVehicleHireSerializer(VehicleActionSerializer):
    vehicle_name = serializers.SerializerMethodField()
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.get_queryset())

    class Meta:
        model = VehicleHire
        fields = '__all__'

    def get_vehicle_name(self, obj):
        vehicle = obj.vehicle
        return f'{vehicle.make} {vehicle.model}'
