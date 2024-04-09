from rest_framework import serializers

from cases.models import CaseNote


class CaseNoteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseNote
        fields = ('id', 'user')
