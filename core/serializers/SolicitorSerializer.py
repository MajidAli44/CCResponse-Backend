from rest_framework.serializers import ModelSerializer

from core.models import ExternalParty


class SolicitorSerializer(ModelSerializer):
    class Meta:
        model = ExternalParty
        fields = ('id', 'name', 'ref')
