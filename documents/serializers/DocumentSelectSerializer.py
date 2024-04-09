from rest_framework import serializers

from documents.models import DocumentTemplates


class DocumentSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentTemplates
        fields = ('id', )
