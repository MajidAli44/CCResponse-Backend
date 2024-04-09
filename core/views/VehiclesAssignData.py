from datetime import date

from django.db.models import Q, Value
from django.db.models.functions import Concat
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Vehicle, VehicleHire


class VehiclesAssignData(APIView):
    def get(self, request, *args, **kwargs):
        qs = Vehicle.objects.all()

        if 'owner' in request.query_params:
            vehicle_owner = request.query_params['owner']
            if vehicle_owner not in Vehicle.Owner.labels:
                return Response('Unknown vehicle owner', status=400)
            qs = qs.filter(owner=vehicle_owner)

        if 'status' in request.query_params and (vehicle_status := request.query_params['status']):
            vehicles_with_hires_ids = VehicleHire.objects.filter(
                Q(end_date__isnull=True) | Q(end_date__gte=date.today()),
                start_date__lte=date.today(), vehicle_id__isnull=False
            ).values_list('vehicle_id', flat=True)

            booked_vehicles_q = Q(pk__in=vehicles_with_hires_ids)
            status_name_to_filter_dict = {
                'Booked': {
                    'q': booked_vehicles_q
                },
                'Available': {
                    'is_active': True, 'is_sold': False, 'q': ~booked_vehicles_q
                },
                'Sold': {
                    'is_active': True, 'is_sold': True, 'q': ~booked_vehicles_q
                }
            }

            if vehicle_status not in status_name_to_filter_dict:
                return Response(
                    f'Unknown vehicle status. Available statuses are: {",".join(list(status_name_to_filter_dict))}'
                )

            filter_dict = status_name_to_filter_dict[vehicle_status]
            q = filter_dict.pop('q')
            qs = qs.filter(q, **filter_dict)

        return Response(
            qs.annotate(
                name=Concat('make', Value(' '), 'model', Value(' '), 'vrn')
            ).values('id', 'name'),
            status=status.HTTP_200_OK
        )
