from rest_framework import serializers

from cases.models import Case


class LetterClientPAVDocumentSerializer(serializers.ModelSerializer):

    client_name = serializers.CharField(source='client.name', allow_null=True)
    client_address = serializers.SerializerMethodField()
    client_vrn = serializers.CharField(source='client.vehicle.vrn', allow_null=True)
    accident_date = serializers.DateField(source='accident.accident_date', allow_null=True)
    client_insurer = serializers.CharField(source='client.insurer.name', allow_null=True)

    class Meta:
        model = Case
        fields = ('client_name', 'client_address', 'client_vrn', 'accident_date', 'client_insurer')

    def get_client_address(self, obj):
        if obj.client:
            if obj.client.address:
                split_address = obj.client.address.split('\n')
                if len(split_address) > 1:
                    return ', '.join(split_address)
                return obj.client.address
        return None
