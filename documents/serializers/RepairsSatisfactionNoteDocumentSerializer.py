from datetime import date

from rest_framework import serializers

from cases.models import Case


class RepairsSatisfactionNoteDocumentSerializer(serializers.ModelSerializer):

    current_date = serializers.SerializerMethodField()
    client_name = serializers.CharField(source='client.name', allow_null=True)
    client_vrn = serializers.CharField(source='client.vehicle.vrn', allow_null=True)
    client_vehicle_make = serializers.CharField(source='client.vehicle.make', allow_null=True)
    client_vehicle_model = serializers.CharField(source='client.vehicle.model', allow_null=True)
    accident_date = serializers.DateField(source='accident.accident_date', allow_null=True)
    client_address = serializers.CharField(source='client.address', allow_null=True)

    class Meta:
        model = Case
        fields = (
            'current_date', 'client_name', 'client_vrn', 'client_vehicle_model', 'client_vehicle_make',
            'accident_date', 'client_address'
        )

    def get_current_date(self, _obj):
        return date.today().strftime("%d/%m/%Y")
