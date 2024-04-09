from decimal import Decimal as D

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Vehicle


class PartyVehicleSerializer(ModelSerializer):
    id = serializers.IntegerField(required=False)
    url = serializers.HyperlinkedIdentityField(view_name="vehicles-detail")
    daily_hire_rate = serializers.DecimalField(
        decimal_places=2, max_digits=15, required=False, default=D(0.00)
    )

    class Meta:
        model = Vehicle
        fields = ('id', 'url', 'vrn', 'make', 'model', 'mot_due', 'tax_due', 'daily_hire_rate')
