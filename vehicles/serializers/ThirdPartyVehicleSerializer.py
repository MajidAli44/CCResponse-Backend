from rest_framework import serializers

from vehicles.models import ThirdPartyVehicle


class ThirdPartyVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdPartyVehicle
        fields = ('id', 'vrn', 'make_model', 'mot_expiry', 'tax_expiry')
