from rest_framework import serializers

from documents.models import DocumentTemplates


class DocumentTemplatesSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:
        model = DocumentTemplates
        fields = ('id', 'case', 'user', 'name', 'empty_fields', 'document_need_sign', 'template_name', 'created_at', 'updated_at')

    def get_user(self, obj):
        if obj.user:
            return obj.user.fullname
        return 'CC Response System'
