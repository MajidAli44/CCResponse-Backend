from django_filters import Filter
from django_filters.constants import EMPTY_VALUES
from rest_framework.exceptions import ValidationError

from vehicles.services import HireVehicleService
hire_vehicle_service = HireVehicleService()


class HireVehicleStatusFilter(Filter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        filter_param = hire_vehicle_service.filter_value_mapper(value)
        if not filter_param:
            raise ValidationError({
                'detail': f'{value} not in [booked, available, sold]'
            })
        return qs.filter(filter_param).distinct()
