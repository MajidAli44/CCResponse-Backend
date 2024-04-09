import django_filters
from django_filters import FilterSet

from cases.models import FollowUp


class FollowupFilter(FilterSet):
    case = django_filters.NumberFilter(field_name='case')

    class Meta:
        model = FollowUp
        fields = ['case', 'title']
