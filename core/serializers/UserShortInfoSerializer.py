from rest_framework.serializers import ModelSerializer

from core.models import User


class UserShortInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'fullname')
