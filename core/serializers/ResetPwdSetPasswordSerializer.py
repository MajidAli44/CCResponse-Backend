from rest_framework import serializers
from rest_framework.exceptions import APIException

from .ResetPwdTokenVerifySerializer import ResetPwdTokenVerifySerializer


class ResetPwdSetPasswordSerializer(ResetPwdTokenVerifySerializer):

    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise APIException({
                'password': 'Password does not match'
            })
        return attrs
