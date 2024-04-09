from parties.models import Provider
from parties.serializers import ProviderSerializer

from .AbstractExtraPartyViewSet import AbstractExtraPartyViewSet


class ProviderViewSet(AbstractExtraPartyViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all().order_by('-created_at')
