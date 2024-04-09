from rest_framework import serializers

from cases.models import Case


class WitnessRequestingStatementDocumentSerializer(serializers.ModelSerializer):

    client_name = serializers.CharField(source='client.name', allow_null=True)
    client_vrn = serializers.CharField(source='client.vehicle.vrn', allow_null=True)
    accident_date = serializers.DateField(source='accident.accident_date', allow_null=True)

    class Meta:
        model = Case
        fields = ('client_name', 'client_vrn', 'accident_date')
