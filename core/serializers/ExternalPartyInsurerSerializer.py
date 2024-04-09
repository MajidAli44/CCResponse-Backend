from rest_framework.serializers import ModelSerializer

from core.models import ExternalParty


class ExternalPartyInsurerSerializer(ModelSerializer):
    class Meta:
        model = ExternalParty
        fields = ('id', 'name', 'ref', 'phone_number', 'email')
