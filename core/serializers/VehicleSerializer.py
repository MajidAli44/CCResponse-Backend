from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Vehicle


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            'id', 'vrn', 'make', 'model', 'service_due', 'date_purchased', 'price_purchased',
            'tax_cost', 'tax_due', 'mot_due', 'mot_cost', 'notes', 'daily_hire_rate', 'daily_storage_rate',
            'owner'
        )
        extra_kwargs = {
            'owner': {'required': False}
        }

    def validate(self, attrs):
        if not any(attrs.values()):
            raise serializers.ValidationError('at least one field must be provided.')
        return attrs

    def create(self, validated_data):
        if 'owner' not in validated_data:
            validated_data['owner'] = Vehicle.Owner.company
        return Vehicle.objects.create(**validated_data)
