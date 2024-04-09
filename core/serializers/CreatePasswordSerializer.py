from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, APIException


class CreatePasswordSerializer(serializers.Serializer):

    token = serializers.CharField(required=True)
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
        else:
            try:
                validate_password(password=attrs['password'])
            except ValidationError as error:
                raise APIException({
                    'password': error
                })
        return attrs
