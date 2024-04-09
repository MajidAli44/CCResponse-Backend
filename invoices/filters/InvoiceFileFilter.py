import django_filters
from django_filters.rest_framework import FilterSet

from cases.models import Case


class InvoiceFileFilter(FilterSet):
    settlement_status = django_filters.ChoiceFilter(choices=Case.CaseStatusDescription.choices, field_name='status_description')

    class Meta:
        model = Case
        fields = ['settlement_status']
