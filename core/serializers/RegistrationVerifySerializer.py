from rest_framework import serializers


class RegistrationVerifySerializer(serializers.Serializer):

    token = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
