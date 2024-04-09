from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from core.models import User


class FileHandlerSerializer(WritableNestedModelSerializer):
    name = serializers.ReadOnlyField(source='get_full_name')

    class Meta:
        model = User
        fields = ('fullname', 'name', 'id')
