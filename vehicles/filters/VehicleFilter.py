from django_filters import FilterSet

from vehicles.models import HireVehicle
from .HireVehicleStatusFilter import HireVehicleStatusFilter


class VehicleFilter(FilterSet):
    status = HireVehicleStatusFilter()

    class Meta:
        model = HireVehicle
        fields = ('status',)
