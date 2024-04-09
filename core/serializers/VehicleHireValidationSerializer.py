from rest_framework import serializers

from core.models import VehicleHireValidation


class VehicleHireValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleHireValidation
        fields = '__all__'
