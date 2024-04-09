from rest_framework import serializers

from vehicles.models import ClientVehicle


class ClientVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientVehicle
        fields = ('id', 'vrn', 'make_model', 'mot_expiry', 'tax_expiry')
