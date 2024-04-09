from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, APIException


class PasswordChangeSerializer(serializers.Serializer):

    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_new_password']:
            raise APIException({
                'new_password': 'Password does not match'
            })
        else:
            try:
                validate_password(password=attrs['new_password'])
            except ValidationError as error:
                raise APIException({
                    'new_password': error
                })
        return attrs
