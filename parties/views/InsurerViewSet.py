from parties.models import Insurer
from parties.serializers import InsurerSerializer

from .AbstractExtraPartyViewSet import AbstractExtraPartyViewSet


class InsurerViewSet(AbstractExtraPartyViewSet):
    serializer_class = InsurerSerializer
    queryset = Insurer.objects.all().order_by('-created_at')
