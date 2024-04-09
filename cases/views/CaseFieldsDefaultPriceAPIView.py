from rest_framework.generics import (
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated

from cases.models import CaseFieldsDefaultPrice
from cases.serializers import CaseFieldsDefaultPriceSerializer


class CaseFieldsDefaultPriceAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CaseFieldsDefaultPriceSerializer

    def get_object(self):
        return CaseFieldsDefaultPrice.objects.last()
