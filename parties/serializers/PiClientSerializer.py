from rest_framework import serializers

from parties.models import PiClient


class PiClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiClient
        fields = ('id', 'name', 'solicitor_ref', 'fee', 'pi_detail')
