from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Customer


class VehicleHireCustomerSerializer(ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=200, required=False)
    address = serializers.CharField(source='address.address', read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone_number', 'email', 'date_of_birth', 'address',
                  'license_number', 'ni_number', 'notes')
