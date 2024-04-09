from rest_framework import serializers


class DocumentDownloadResponseSerializer(serializers.Serializer):

    url = serializers.URLField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
