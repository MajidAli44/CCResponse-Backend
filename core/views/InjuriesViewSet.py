from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Injury
from core.serializers import InjurySerializer
from core.utils import PaginatedQSMixin


class InjuriesViewSet(ModelViewSet, PaginatedQSMixin):
    serializer_class = InjurySerializer
    injuries_fields = Injury.__dict__.copy()

    def get_queryset(self):
        return Injury.objects.get_queryset()

    def list(self, request, *args, **kwargs):
        return self.default_list(self.injuries_fields, request, *args, **kwargs)

    @action(methods=['get'], url_path='statuses', detail=False)
    def statuses(self, request, *args, **kwargs):
        return Response(Injury.Status.choices, status=status.HTTP_200_OK)

    @action(methods=['get'], url_path='types', detail=False)
    def types(self, request, *args, **kwargs):
        return Response(Injury.Type.choices, status=status.HTTP_200_OK)
