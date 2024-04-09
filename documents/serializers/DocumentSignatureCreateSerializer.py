from rest_framework import serializers

from documents.models import DocumentSignature


class DocumentSignatureCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentSignature
        fields = ('id', 'document', 'recipient_name', 'recipient', 'message', 'status')
        read_only_fields = ('id', 'status')