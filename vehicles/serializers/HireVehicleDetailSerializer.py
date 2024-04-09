from datetime import date

from django.db.models import Q
from rest_framework import serializers

from cases.models import HireDetail
from vehicles.models import HireVehicle


class HireVehicleDetailSerializer(serializers.ModelSerializer):

    is_booked = serializers.SerializerMethodField()

    class Meta:
        model = HireVehicle
        fields = (
            'id', 'vrn', 'make_model', 'mot_expiry', 'tax_expiry',
            'registration', 'date_purchased', 'purchase_price', 'service_due',
            'tax_cost', 'mot_cost', 'notes', 'is_sold', 'is_booked'
        )
        read_only_fields = ('is_booked',)

    def get_is_booked(self, _obj):
        vehicles_with_hires_ids = HireDetail.objects.filter(
            Q(end_date__isnull=True) | Q(end_date__gt=date.today()),
            start_date__lte=date.today(), vehicle_id__isnull=False, case__isnull=False
        ).values_list('vehicle_id', flat=True)

        if not _obj.is_sold and _obj.pk in vehicles_with_hires_ids:
            return True
        return False
