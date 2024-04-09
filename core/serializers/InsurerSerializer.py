from rest_framework import serializers

from core.models import ExternalParty


class InsurerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = ExternalParty
        fields = ('id', 'name', 'email', 'phone_number', 'is_active')

    def create(self, validated_data):
        return ExternalParty.objects.create(
            **validated_data,
            role=ExternalParty.Role.insurer,
            is_third_party=False
        )
