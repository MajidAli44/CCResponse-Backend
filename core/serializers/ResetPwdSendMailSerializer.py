from rest_framework import serializers


class ResetPwdSendMailSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255, required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
