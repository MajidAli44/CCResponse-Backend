from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import CaseNote


class CaseNoteSerializer(ModelSerializer):
    worker = serializers.CharField(source='worker.fullname')

    class Meta:
        model = CaseNote
        fields = ('id', 'created_at', 'worker', 'note')
