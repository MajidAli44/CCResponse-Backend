from rest_framework import serializers

from vehicles.models import VehicleFieldsDefaultPrice


class VehicleFieldsDefaultPriceSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(VehicleFieldsDefaultPriceSerializer, self).__init__(*args, **kwargs)
        self.fields.pop('id')

    class Meta:
        model = VehicleFieldsDefaultPrice
        fields = '__all__'
