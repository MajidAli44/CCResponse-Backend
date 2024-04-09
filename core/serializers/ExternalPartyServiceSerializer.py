from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from core.models import ExternalParty, ExternalPartyService


class ExternalPartyServiceSerializer(ModelSerializer):
    id = serializers.IntegerField(source='external_party.id', required=False)
    name = serializers.CharField(source='external_party.name', required=False)
    role = serializers.ChoiceField(source='external_party.role', choices=ExternalParty.Role.choices, required=False)
    email = serializers.EmailField(source='external_party.email', required=False, allow_blank=True, allow_null=True)
    ref = serializers.CharField(source='external_party.ref', required=False, allow_blank=True)
    phone_number = serializers.CharField(source='external_party.phone_number', required=False, allow_blank=True)
    introducer_fee = serializers.DecimalField(source='external_party.introducer_fee', required=False, allow_null=True,
                                              decimal_places=2, max_digits=15)

    class Meta:
        model = ExternalPartyService
        fields = ('id', 'name', 'role', 'email', 'ref', 'phone_number', 'introducer_fee')

    def validate(self, attrs):
        external_party = attrs.get('external_party', {})
        tp_id = external_party.get('id', None)
        name = external_party.get('name', None)
        if not tp_id and not name:
            raise serializers.ValidationError({
                'name': 'need to specify either the existing party or the data to create a new one.'
            })
        elif name and not external_party.get('role'):
            raise serializers.ValidationError({
                'role': 'to create an external party need to specify at least the name and role.'
            })

        qs = ExternalParty.objects.filter(name=name)
        if tp_id:
            qs = qs.exclude(id=tp_id)
        if name and qs.exists():
            raise ValidationError({'name': 'party with this name already exists.'})
        return attrs

    def validate_id(self, value):
        if not ExternalParty.objects.filter(pk=value, is_third_party=False).exists():
            raise serializers.ValidationError("this party doesn't exist or is not an external party.")
        return value
