from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from core.models import User


class UserPublicSerializer(ModelSerializer):
    name = serializers.ReadOnlyField(source='get_full_name')

    class Meta:
        model = User
        fields = ('id', 'name', 'fullname')
