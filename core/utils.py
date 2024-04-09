from collections.abc import Iterable
import dateutil.parser

from django.conf import settings
from django.db.models import Q, Count
from django.db.models.fields import DateField, AutoField
from django.db.models.fields.related import ManyToManyField, ForeignKey

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


class PaginatedQSMixin:
    def get_serializer(self, *args, **kwargs):
        raise Exception('get_serializer is not implemented')

    def get_queryset(self):
        raise Exception('get_queryset is not implemented')

    def default_list(self, fields, request, *args, **kwargs):
        qs = self.get_queryset()

        query_params = request.query_params.copy()

        (
            truncated_qs, count, _,
            old_query_params, page, page_size, total_aggregates_results
        ) = self.apply_query_params(query_params, qs, fields)

        data = self.build_paginated_response_without_results(
            request, old_query_params, count, page, page_size, total_aggregates_results
        )

        data['results'] = self.get_serializer(truncated_qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    @staticmethod
    def apply_query_params(
            query_params, initial_queryset, qs_fields, search_fields=None,
            additional_counts_field=None, additional_counts_map_value_to_name=None,
            additional_count_fields_to_exclude_from_filter_config=None, total_aggregates=None
    ):
        if search_fields is None:
            search_fields = []

        query_params = query_params.copy()

        # Should pop page before we create old_query_params for pagination purposes
        page = query_params.pop('page', 1)
        if isinstance(page, list):
            page = page[0]
        try:
            page = int(page)
        except (TypeError, ValueError):
            raise ValidationError('Cannot convert page to integer')
        if page < 1:
            raise ValidationError('Page should be greater than 1')

        old_query_params = query_params.copy()

        page_size = query_params.pop('page-size', settings.CASES_DEFAULT_PAGE_SIZE)
        if isinstance(page_size, list):
            page_size = page_size[0]
        try:
            page_size = int(page_size)
        except (TypeError, ValueError):
            raise ValidationError('Cannot convert page-size to integer')

        search = query_params.pop('search', None)
        if isinstance(search, list):
            search = search[0]
        search_conf = None
        if search:
            for field in search_fields:
                search_conf = (
                    Q(**{f'{field}__contains': search})
                    if search_conf is None
                    else (search_conf | Q(**{f'{field}__icontains': search}))
                )

        # Get order_by fields
        orderby_args = []
        for order_key, order_value in filter(
                lambda pair: pair[0].startswith('orderby'),
                list(query_params.items())
        ):
            query_params.pop(order_key, None)
            orderby_field = order_key[len('orderby_'):]

            if orderby_field not in qs_fields:
                raise ValidationError(f"Object doesn't have {orderby_field} orderby field")
            if order_value != '-1' and order_value != '1':
                raise ValidationError('Orderby value should be 1 or -1')

            orderby_args.append(f"{'' if order_value == '1' else '-'}{orderby_field}")

        filter_config = {}
        filter_config_q = []
        for filter_key, filter_value in query_params.items():
            if isinstance(filter_value, Q):
                filter_config_q.append(filter_value)
                continue

            filter_field = filter_key.split('__', 1)[0]
            if filter_field not in qs_fields:
                continue

            if isinstance(qs_fields[filter_field].field, DateField):
                try:
                    filter_value = dateutil.parser.isoparse(filter_value)
                except ValueError as ex:
                    raise ValidationError(f'{filter_key}: {ex.__str__()}')

            if isinstance(filter_value, str) and ',' in filter_value:
                filter_key = f'{filter_key}__in'
                filter_value = filter_value.split(',')

            field_type = qs_fields[filter_field].field
            if (
                isinstance(field_type, (ManyToManyField, AutoField))
                or isinstance(field_type, ForeignKey) and filter_key.endswith('_id')
                or filter_key.endswith('_id__in')
            ):
                temp_list = filter_value[:] if filter_key.endswith('__in') else [filter_value]
                for value in temp_list:
                    try:
                        int(value)
                    except (TypeError, ValueError):
                        raise ValidationError(
                            f"Field {filter_key} expected a number or list of numbers, but got {filter_value}."
                        )

            filter_config[filter_key] = filter_value

        qs = initial_queryset
        if search_conf:
            qs = qs.filter(
                search_conf
            )

        additional_counts_result = None
        if additional_counts_field:
            if additional_counts_map_value_to_name is None:
                raise Exception(
                    "You should specify additional_counts_map_value_to_name if you specify additional_counts_field!"
                )
            filter_config_additional = filter_config.copy()

            for field in (additional_count_fields_to_exclude_from_filter_config or []):
                keys_matching = [
                    key for key in filter_config_additional
                    if key.startswith(field)
                ]
                for key in keys_matching:
                    filter_config_additional.pop(key, None)

            if isinstance(additional_counts_field, Iterable) and not isinstance(additional_counts_field, str):
                for field in additional_counts_field:
                    filter_config_additional.pop(field, None)
            else:
                filter_config_additional.pop(additional_counts_field, None)

            for k, v in additional_counts_map_value_to_name.items():
                if isinstance(v, dict):
                    continue
                elif isinstance(additional_counts_field, Iterable) and not isinstance(additional_counts_field, str):
                    additional_counts_map_value_to_name[k] = {
                        next(iter(additional_counts_field)): v
                    }
                    print("Warning!!! additional_counts_field first argument is taken!!!")
                else:
                    additional_counts_map_value_to_name[k] = {additional_counts_field: v}

            aggregate_dict = {}
            for k, v in additional_counts_map_value_to_name.items():
                d = {}
                q = None
                for k_d, v_d in v.items():
                    if isinstance(v_d, Q):
                        q = q & v_d if q else v_d
                    else:
                        d[k_d] = v_d
                q = q & Q(**d) if q else Q(**d)
                aggregate_dict[k] = Count('id', filter=q)
            additional_counts_result = qs.filter(**filter_config_additional).aggregate(**aggregate_dict)

        if filter_config or filter_config_q:
            qs = qs.filter(
                *filter_config_q,
                **filter_config
            )

        total_aggregates_results = qs.aggregate(
            count=Count('id'),
            **(total_aggregates or {})
        )

        count = total_aggregates_results['count']

        if orderby_args:
            qs = qs.order_by(*orderby_args)

        truncated_qs = qs[page_size * (page - 1): page_size * page]
        return (
            truncated_qs, count, additional_counts_result,
            old_query_params, page, page_size, total_aggregates_results
        )

    @staticmethod
    def build_paginated_response_without_results(
        request, old_query_params, count, page, page_size, total_aggregates_results=None
    ):
        absolute_path = request.build_absolute_uri(request.path)
        pagination_query_params = (
            f"{'&'.join([f'{key}={value}' for key, value in old_query_params.items()])}"
            if old_query_params else ""
        )
        pagination_url_template = "%s?%s%s" % (
            absolute_path,
            pagination_query_params,
            "&page={}" if pagination_query_params else "page={}"
        )

        start_page = 1
        end_page = (count // page_size) + (1 if count % page_size else 0)
        return {
            'count': count,
            'page': page,
            'page_size': page_size,
            'current': pagination_url_template.format(page),
            'start': pagination_url_template.format(1),
            'end': pagination_url_template.format(end_page or 1),
            'next': pagination_url_template.format(page + 1) if page < end_page else None,
            'previous': pagination_url_template.format(page - 1) if page > start_page else None,
            **(total_aggregates_results or {})
        }
