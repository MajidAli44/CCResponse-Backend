from rest_framework import serializers


class ExtraPartyCountSerializer(serializers.Serializer):
    """ Serializer for count of all extra parties """

    solicitor_count = serializers.IntegerField(default=0)
    insurer_count = serializers.IntegerField(default=0)
    introducer_count = serializers.IntegerField(default=0)
    provider_count = serializers.IntegerField(default=0)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
