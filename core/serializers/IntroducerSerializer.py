from rest_framework.serializers import ModelSerializer

from core.models import ExternalParty


class IntroducerSerializer(ModelSerializer):
    class Meta:
        model = ExternalParty
        fields = ('id', 'name', 'introducer_fee')
