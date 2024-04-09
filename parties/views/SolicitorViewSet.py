from parties.models import Solicitor
from parties.serializers import SolicitorSerializer

from .AbstractExtraPartyViewSet import AbstractExtraPartyViewSet


class SolicitorViewSet(AbstractExtraPartyViewSet):
    serializer_class = SolicitorSerializer
    queryset = Solicitor.objects.all().order_by('-created_at')
