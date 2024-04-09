from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from parties.models import Client
from vehicles.serializers import ClientVehicleSerializer


class ClientSerializer(WritableNestedModelSerializer):
    vehicle = ClientVehicleSerializer(required=False, allow_null=True)

    class Meta:
        model = Client
        fields = (
            'id', 'name', 'phone_number', 'email', 'notes', 'address', 'postcode',
            'date_of_birth', 'license_number', 'ni_number', 'insurer',
            'vehicle'
        )
