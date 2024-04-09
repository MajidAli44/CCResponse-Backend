from parties.models import Introducer
from parties.serializers import IntroducerSerializer

from .AbstractExtraPartyViewSet import AbstractExtraPartyViewSet


class IntroducerViewSet(AbstractExtraPartyViewSet):
    serializer_class = IntroducerSerializer
    queryset = Introducer.objects.all().order_by('-created_at')
