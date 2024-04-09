from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from documents.models import Document


class DocumentUploadDownloadSerializer(serializers.Serializer):

    case_id = serializers.IntegerField(required=False)
    introducer_id = serializers.IntegerField(required=False)
    solicitor_id = serializers.IntegerField(required=False)

    document_ids = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False, allow_null=False, required=True
    )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        if attrs.get('case_id') is None and attrs.get('introducer_id') is None and attrs.get('solicitor_id') is None:
            raise ValidationError({'message': 'please fill field case_id or introducer_id or solicitor_id'})

        document_ids = set(attrs.get('document_ids'))

        valid_document_ids = []
        if attrs.get('case_id') is not None:
            valid_document_ids = set(Document.objects.filter(id__in=document_ids, case_id=attrs.get('case_id')).values_list('id', flat=True))
        elif attrs.get('introducer_id') is not None:
            valid_document_ids = set(Document.objects.filter(id__in=document_ids, case_id=attrs.get('case_id')).values_list('id', flat=True))
        elif attrs.get('solicitor_id') is not None:
            valid_document_ids = set(Document.objects.filter(id__in=document_ids, case_id=attrs.get('case_id')).values_list('id', flat=True))

        not_valid_ids = document_ids - valid_document_ids

        if not_valid_ids:
            raise ValidationError({'message': f'{list(not_valid_ids)} are invalid document id'})

        return attrs
