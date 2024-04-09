from rest_framework import serializers


class EmailVerifySerializer(serializers.Serializer):

    token = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
