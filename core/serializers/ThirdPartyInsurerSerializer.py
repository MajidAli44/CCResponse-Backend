from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from core.models import ExternalParty


class ThirdPartyInsurerSerializer(ModelSerializer):
    name = serializers.CharField(required=False, allow_blank=True)
    id = serializers.IntegerField(required=False)

    class Meta:
        model = ExternalParty
        fields = ('id', 'name', 'phone_number', 'email', 'ref')

    def validate_id(self, value):
        if not ExternalParty.objects.filter(pk=value, is_third_party=True, role=ExternalParty.Role.insurer).exists():
            raise serializers.ValidationError("this party doesn't exist or is not a third party insurer.")
        return value

    def validate(self, attrs):
        if not attrs.get('id') and not attrs.get('name'):
            raise serializers.ValidationError({
                'name': 'need to specify either the existing party or the data to create a new one.'
            })

        name = attrs.get('name', None)
        tp_id = attrs.get('id', None)
        qs = ExternalParty.objects.filter(name=name)
        if tp_id:
            qs = qs.exclude(id=tp_id)
        if name and qs.exists():
            raise ValidationError({
                'name': 'party with this name already exists.'
            })
        return attrs
