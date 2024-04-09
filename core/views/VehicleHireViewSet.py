from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Customer, VehicleHire, VehicleAction
from core.serializers import VehicleHireSerializer
from core.utils import PaginatedQSMixin


class VehicleHireViewSet(ModelViewSet, PaginatedQSMixin):
    serializer_class = VehicleHireSerializer
    search_fields = ['customer__name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hire_fields = VehicleHire.__dict__.copy()
        self.hire_fields.update(
            VehicleAction.__dict__.copy()
        )
        self.hire_fields.update({
            'customer__name': Customer.name
        })

    def get_queryset(self):
        return VehicleHire.objects.get_queryset()

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()

        query_params = request.query_params.copy()

        order_by_field_names_to_fields = {
            'client_name': 'customer__name',
            'booking_range': 'start_date'
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
        ) = self.apply_query_params(query_params, qs, self.hire_fields, self.search_fields)

        data = self.build_paginated_response_without_results(request, old_query_params, count, page, page_size)

        data['additional_counts'] = additional_counts
        data['results'] = [
            {
                'id': hire_data['id'],
                'created_at': hire_data['created_at'].strftime(settings.DEFAULT_DATETIME_FORMAT),
                'client_name': hire_data['customer__name'],
                'booking_range': "{} - {}".format(
                    hire_data['start_date'] and hire_data['start_date'].strftime(settings.DEFAULT_DATE_FORMAT) or '',
                    hire_data['end_date'] and hire_data['end_date'].strftime(settings.DEFAULT_DATE_FORMAT) or '',
                ).strip(),
                'start_date': hire_data['start_date'] and hire_data['start_date'].isoformat(),
                'end_date': hire_data['end_date'] and hire_data['end_date'].isoformat()
            } for hire_data in truncated_qs.values(
                'id', 'created_at', 'customer__name',
                'start_date', 'end_date'
            )
        ]

        return Response(data, status=status.HTTP_200_OK)
