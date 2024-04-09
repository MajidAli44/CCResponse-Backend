from rest_framework import serializers

from cases.models import ClawbackDetail


class ClawbackDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClawbackDetail
        fields = (
            'date', 'reason', 'replace_name', 'intro_rep_case', 'we_rep_case',
            'chase_date', 'replaced'
        )
