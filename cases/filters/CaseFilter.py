import django_filters
from django.db.models import Q
from django_filters import FilterSet

from cases.models import Case


class CaseFilter(FilterSet):
    acc_date_from = django_filters.DateFilter(
        field_name='accident__accident_date', lookup_expr="gte",
        input_formats=['%d/%m/%Y']
    )
    acc_date_to = django_filters.DateFilter(
        field_name='accident__accident_date', lookup_expr="lte",
        input_formats=['%d/%m/%Y']
    )
    instruction_date_from = django_filters.DateFilter(
        field_name='instruction_date', lookup_expr="gte", input_formats=['%d/%m/%Y']
    )
    instruction_date_to = django_filters.DateFilter(
        field_name='instruction_date', lookup_expr="lte", input_formats=['%d/%m/%Y']
    )
    status = django_filters.MultipleChoiceFilter(choices=Case.CaseStatuses.choices, field_name='status')
    payment_status = django_filters.ChoiceFilter(choices=Case.PaymentStatuses.choices)
    client_name = django_filters.CharFilter(field_name="client__name", lookup_expr='icontains')
    client_phone_number = django_filters.CharFilter(field_name="client__phone_number", lookup_expr='icontains')
    introducer_name = django_filters.CharFilter(field_name="introducer__name", lookup_expr='icontains')
    tp_insurer_name = django_filters.CharFilter(field_name="third_party__insurer__name", lookup_expr='icontains')
    client_notes = django_filters.CharFilter(field_name="client__notes", lookup_expr='icontains')
    services = django_filters.BaseInFilter(field_name="services", lookup_expr='overlap')
    providers = django_filters.CharFilter(method='filter_by_providers')
    hire_categories = django_filters.BaseInFilter(field_name="hire_detail__hire_categories", lookup_expr='overlap')
    status_description = django_filters.CharFilter(method='filter_by_status_description')

    class Meta:
        model = Case
        fields = [
            'instruction_date_from', 'instruction_date_to', 'acc_date_from',
            'acc_date_to', 'status', 'payment_status', 'client_name',
            'client_phone_number', 'introducer_name', 'tp_insurer_name',
            'client_notes', 'services', 'providers', 'status_description'
        ]

    def filter_by_providers(self, queryset, name, value):
        values = value.split(',')
        return queryset.filter(
            Q(hire_detail__provider__in=values) |
            Q(storage_detail__provider__in=values) |
            Q(pi_detail__provider__in=values)
        )
    
    def filter_by_status_description(self, queryset, name, value):
        values = value.split(',')
        return queryset.filter(
            Q(status_description__in=values) |
            Q(status_description__isnull=True)
        )
