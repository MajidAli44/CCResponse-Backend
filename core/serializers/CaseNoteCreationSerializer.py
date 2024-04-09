from rest_framework.serializers import ModelSerializer

from core.models import CaseNote


class CaseNoteCreationSerializer(ModelSerializer):
    class Meta:
        model = CaseNote
        fields = ('note',)

    def create(self, validated_data):
        request = self.context['request']
        case_id = self.context['case_id']
        return CaseNote.objects.create(case_id=case_id, worker=request.user, note=validated_data['note'])
