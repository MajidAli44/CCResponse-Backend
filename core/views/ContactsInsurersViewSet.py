from rest_framework.viewsets import ModelViewSet

from core.models import ExternalParty
from core.serializers import InsurerSerializer


class ContactsInsurersViewSet(ModelViewSet):
    serializer_class = InsurerSerializer
    authentication_classes = []
    permission_classes = []
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

    def get_queryset(self):
        return ExternalParty.objects.filter(role=ExternalParty.Role.insurer)
