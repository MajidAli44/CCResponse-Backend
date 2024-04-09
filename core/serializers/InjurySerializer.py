from rest_framework import serializers

from core.models import ExternalParty, Injury


class InjurySerializer(serializers.ModelSerializer):
    class Meta:
        model = Injury
        fields = ('id', 'case', 'solicitor', 'date', 'status', 'type')

    def validate_solicitor(self, val):
        if not val:
            raise serializers.ValidationError({'solicitor': 'Solicitor is not specified'})
        if val.role != ExternalParty.Role.solicitor:
            raise serializers.ValidationError({'solicitor': 'Specified external party is not solicitor'})
        return val
