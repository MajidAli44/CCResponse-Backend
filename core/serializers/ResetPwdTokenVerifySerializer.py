from rest_framework import serializers
from core.models import PasswordResetRequest
from core.services import UserService

user_service = UserService


class ResetPwdTokenVerifySerializer(serializers.Serializer):

    token = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate_token(self, token):
        """
        Check reset request token is valid
        """
        user_tokens = PasswordResetRequest.objects.filter(token=token)
        if not user_tokens.exists():
            if not user_service.check_token(user_tokens.last(), token):
                raise serializers.ValidationError(
                    {'token': 'Token does not exist or is already used'}
                )
        return token
