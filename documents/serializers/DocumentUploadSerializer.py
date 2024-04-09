from rest_framework import serializers


from documents.models import Document
from documents.serializers import DocumentSignatureCreateSerializer


class CaseUploadDocumentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    document_signature = DocumentSignatureCreateSerializer(read_only=True)

    class Meta:
        model = Document
        fields = ('id', 'file', 'case', 'user', 'created_at', 'empty_fields', 'document_signature', 'display_document_in_table',
                  'document_need_sign', 'name', 'is_auto')
        read_only_fields = (
            'id', 'empty_fields', 'display_document_in_table', 'document_need_sign', 'name'
        )

    def get_user(self, obj):
        if obj.user:
            return obj.user.fullname
        return 'CC Response'
