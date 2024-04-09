from rest_framework import serializers

from cases.models import CaseNote


class CaseNoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseNote
        fields = ('id', 'case', 'user', 'note', 'created_at')
        extra_kwargs = {
            'created_at': {'read_only': True}
        }
