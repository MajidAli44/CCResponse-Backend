from rest_framework import serializers

from parties.models import Insurer


class InsurerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurer
        fields = ('id', 'name', 'phone_number', 'email')
