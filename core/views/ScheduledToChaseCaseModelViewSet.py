from datetime import date

from rest_framework.viewsets import ModelViewSet

from core.models import ScheduledToChaseCase
from core.serializers import ScheduledToChaseCaseSerializer


class ScheduledToChaseCaseModelViewSet(ModelViewSet):
    serializer_class = ScheduledToChaseCaseSerializer

    def get_queryset(self):
        return ScheduledToChaseCase.objects.filter(chase_date__lte=date.today()).order_by('chase_date')
