from datetime import date

from django.db.models import Case as DB_Case
from django.db.models import (
    Count, Q, F, Sum, IntegerField, When
)
from django.db.models.functions import Coalesce

from cases.models import HireDetail
from vehicles.models import HireVehicle


class HireVehicleService:
    _model = HireVehicle

    @classmethod
    def get_each_status_count_of_vehicles(cls):
        return cls._model.objects.all().aggregate(
            all_count=Count(F('id'), distinct=True),
            sold_count=Coalesce(Sum(DB_Case(
                When(cls.filter_value_mapper('sold'), then=1),
                output_field=IntegerField(), distinct=True)
            ), 0),
            booked_count=Coalesce(Sum(DB_Case(
                When(cls.filter_value_mapper('booked'), then=1),
                output_field=IntegerField(), distinct=True)
            ), 0),
            available_count=Coalesce(Count(DB_Case(
                When(cls.filter_value_mapper('available'), then=1),
                output_field=IntegerField(), distinct=True)
            ), 0)
        )

    @classmethod
    def filter_value_mapper(cls, filter_value):
        vehicles_with_hires_ids = HireDetail.objects.filter(
            Q(end_date__isnull=True) | Q(end_date__gt=date.today()),
            start_date__lte=date.today(), vehicle_id__isnull=False, case__isnull=False
        ).values_list('vehicle_id', flat=True)
        booked_filter = Q(pk__in=vehicles_with_hires_ids, is_sold=False)
        available_filter = Q(~booked_filter, is_sold=False)

        return {
            'booked': booked_filter,
            'available': available_filter,
            'sold': Q(is_sold=True),
        }.get(filter_value)
