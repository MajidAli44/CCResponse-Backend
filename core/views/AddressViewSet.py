from django.contrib.postgres.search import TrigramSimilarity
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Address
from core.serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        qs = Address.objects.all()
        if 's' in self.request.query_params:
            qs = qs.annotate(
                similarity=TrigramSimilarity('address', self.request.query_params['s'])
            ).filter(similarity__gte=0.05).order_by('-similarity')[:10].values('id', 'address')
        return qs

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return Response(queryset.values())
