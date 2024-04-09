from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import User


class UserDetailSerializer(ModelSerializer):
    is_email_verified = serializers.BooleanField(
        source='email_verify_request.is_verified', read_only=True,
        default=False
    )

    class Meta:
        model = User
        fields = ('id', 'email', 'fullname', 'is_email_verified', 'role')
