from rest_framework import serializers

from cases.models import Case, CaseNote


class CaseListSerializer(serializers.ModelSerializer):
    accident_date = serializers.DateField(source='accident.accident_date', allow_null=True)
    client_name = serializers.CharField(source='client.name', allow_null=True)
    phone_number = serializers.CharField(source='client.phone_number', allow_null=True)
    introducer = serializers.CharField(source='introducer.name', allow_null=True)
    provider = serializers.CharField(source='provider.name', allow_null=True)
    tp_insurer = serializers.CharField(source='third_party.insurer.name', allow_null=True)
    instructed_solicitor = serializers.PrimaryKeyRelatedField(source='pi_detail.solicitor_introduced', read_only=True,
                                                              allow_null=True)
    status = serializers.SerializerMethodField(allow_null=True)
    notes = serializers.SerializerMethodField(allow_null=True)
    current_handler = serializers.CharField(source='file_handler.fullname', allow_null=True)

    class Meta:
        model = Case
        fields = (
            'id', 'cc_ref', 'case_value', 'services', 'instruction_date', 'accident_date', 'client_name',
            'phone_number', 'introducer', 'introducer_fee', 'provider', 'tp_insurer', 'instructed_solicitor',
            'status', 'notes', 'service_providers', 'current_handler'
        )

    def get_status(self, _obj):
        if _obj.status_description is not None:
            return _obj.status_description
        return None

    def get_notes(self, _obj):
        note = CaseNote.objects.filter(case_id=_obj.pk)
        if len(note) > 0:
            note = note.last()
            return note.note
        return None
