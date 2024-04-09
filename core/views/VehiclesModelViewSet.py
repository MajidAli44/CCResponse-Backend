from datetime import date

from django.conf import settings
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet

from core.models import Vehicle, Customer, VehicleHire
from core.serializers import VehicleSerializer
from core.utils import PaginatedQSMixin


class VehiclesModelViewSet(ModelViewSet, PaginatedQSMixin):
    serializer_class = VehicleSerializer
    search_fields = ['customer_vehicle_cases__customer__name']

    def get_queryset(self):
        return Vehicle.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vehicle_fields = Vehicle.__dict__.copy()
        self.vehicle_fields.update(
            {
                'customer_vehicle_cases__customer__name': Customer.name,
                'customer_vehicle_cases__customer_id': Customer.pk,
                'vehicle_storages__start_date': VehicleHire.start_date
            }
        )

    @staticmethod
    def _get_formatted_date(d, fmt):
        return d and d.strftime(fmt)

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset().filter(owner=Vehicle.Owner.company)

        query_params = request.query_params.copy()
        vehicles_with_hires_ids = VehicleHire.objects.filter(
            Q(end_date__isnull=True) | Q(end_date__gte=date.today()),
            start_date__lte=date.today(), vehicle_id__isnull=False
        ).values_list('vehicle_id', flat=True)

        booked_vehicles_q = Q(pk__in=vehicles_with_hires_ids)
        status_name_to_filter_dict = {
            'Booked': {'q': booked_vehicles_q, 'owner': Vehicle.Owner.company},
            'Available': {'is_active': True, 'is_sold': False, 'q': ~booked_vehicles_q, 'owner': Vehicle.Owner.company},
            'Sold': {'is_active': True, 'is_sold': True, 'q': ~booked_vehicles_q, 'owner': Vehicle.Owner.company}
        }

        vehicle_status = None
        if 'status' in query_params:
            vehicle_status = query_params['status']
            del query_params['status']
            query_params.update(
                status_name_to_filter_dict.get(vehicle_status, {})
            )

        order_by_field_names_to_fields = {
            'client_name': 'customer_vehicle_cases__customer__name',
            'booking_range': 'vehicle_storages__start_date'
        }
        for possible_orderby_field in order_by_field_names_to_fields:
            f = f'orderby_{possible_orderby_field}'
            orderby_val = query_params.get(f, None)
            if orderby_val is not None:
                query_params[
                    f'orderby_{order_by_field_names_to_fields[possible_orderby_field]}'
                ] = orderby_val
                del query_params[f]

        (
            truncated_qs, count, additional_counts,
            old_query_params, page, page_size, _
        ) = self.apply_query_params(
            query_params, qs, self.vehicle_fields, self.search_fields, ('is_active', 'is_sold', 'owner'),
            additional_counts_map_value_to_name=status_name_to_filter_dict,
            additional_count_fields_to_exclude_from_filter_config=('pk', 'id')
        )

        if vehicle_status:
            for k in status_name_to_filter_dict.get(vehicle_status, {}).keys():
                old_query_params.pop(k, None)
            old_query_params['status'] = vehicle_status

        data = self.build_paginated_response_without_results(request, old_query_params, count, page, page_size)

        vehicle_ids = truncated_qs.values_list('pk', flat=True)

        vehicle_ids_to_latest_hire_data = {}
        for vehicle_id, start_date, end_date, customer_name in VehicleHire.objects.filter(
                Q(end_date__gte=date.today()) | Q(end_date__isnull=True),
                vehicle_id__in=vehicle_ids
        ).values_list('vehicle_id', 'start_date', 'end_date', 'customer__name'):
            hire_in_dict = vehicle_ids_to_latest_hire_data.get(vehicle_id, None)
            if not hire_in_dict or start_date < hire_in_dict['start_date']:
                vehicle_ids_to_latest_hire_data[vehicle_id] = {
                    'start_date': start_date,
                    'end_date': end_date,
                    'customer_name': customer_name
                }

        data['additional_counts'] = additional_counts
        date_format = settings.DEFAULT_DATE_FORMAT
        data['results'] = []

        for vehicle_data in truncated_qs.values(
                'id', 'created_at', 'make', 'model',
                'date_purchased', 'mot_due', 'tax_due', 'service_due'
        ):
            latest_vehicle_hire_data = vehicle_ids_to_latest_hire_data.get(vehicle_data['id'], {})
            data['results'].append(
                {
                    'id': vehicle_data['id'],
                    'created_at': vehicle_data['created_at'].strftime(settings.DEFAULT_DATETIME_FORMAT),
                    'make': vehicle_data['make'],
                    'model': vehicle_data['model'],
                    'date_purchased': self._get_formatted_date(vehicle_data['date_purchased'], date_format),
                    'mot_due': self._get_formatted_date(vehicle_data['mot_due'], date_format),
                    'tax_due': self._get_formatted_date(vehicle_data['tax_due'], date_format),
                    'service_due': self._get_formatted_date(vehicle_data['service_due'], date_format),
                    'client_name': latest_vehicle_hire_data.get('customer_name', None),
                    'booking_range': "{} - {}".format(
                        self._get_formatted_date(latest_vehicle_hire_data.get('start_date', None), date_format) or '',
                        self._get_formatted_date(latest_vehicle_hire_data.get('end_date', None), date_format) or ''
                    )
                }
            )

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=VehicleSerializer,
        responses={
            status.HTTP_201_CREATED: 'Created',
            status.HTTP_400_BAD_REQUEST: "Bad Request"
        },
        operation_id='company_vehicle_create',
    )
    def create(self, request, *args, **kwargs):
        serializer = VehicleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            obj = serializer.save()
            response = Response(status=status.HTTP_201_CREATED)
            response['Location'] = reverse('vehicles-detail', kwargs={'pk': obj.id})
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

