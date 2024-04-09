from rest_framework import serializers

from core.models import Injury, ExternalParty


class InjuryCaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Injury
        fields = ('id', 'solicitor', 'date', 'status', 'type', 'case')

    def validate_solicitor(self, val):
        if not val:
            raise serializers.ValidationError({'solicitor': 'Solicitor is not specified'})
        if val.role != ExternalParty.Role.solicitor:
            raise serializers.ValidationError({'solicitor': 'Specified external party is not solicitor'})
        return val
