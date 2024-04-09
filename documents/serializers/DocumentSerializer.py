from rest_framework import serializers

from common.services.StorageService import storageService
from documents.models import Document
from documents.serializers.DocumentSignatureCreateSerializer import DocumentSignatureCreateSerializer


class DocumentSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    file_url = serializers.SerializerMethodField()
    document_signature = DocumentSignatureCreateSerializer(read_only=True)

    class Meta:
        model = Document
        read_only_fields = (
            'id', 'empty_fields', 'display_document_in_table', 'document_need_sign', 'name', 'file_url',
            'document_signature'
        )
        fields = (
            'id', 'case', 'user', 'introducer', 'solicitor', 'rel_file_path', 'name', 'empty_fields', 'auto_generated_document',
            'document_need_sign', 'display_document_in_table', 'file_url', 'created_at', 'updated_at', 'document_signature',
        )

    def get_user(self, obj):
        if obj.user:
            return obj.user.fullname
        return 'CC Response System'

    def get_file_url(self, obj):
        if obj.rel_file_path:
            return storageService.get_s3_presigned_url(obj.rel_file_path)
        return None