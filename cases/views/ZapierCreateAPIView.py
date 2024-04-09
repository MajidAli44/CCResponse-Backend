from rest_framework.generics import CreateAPIView

from cases.models import Case
from cases.serializers import CaseCreateSerializer


class ZapierCreateAPIView(CreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseCreateSerializer
    permission_classes = ()
