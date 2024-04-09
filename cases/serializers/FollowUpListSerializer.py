from rest_framework import serializers

from cases.models import FollowUp
from core.serializers import UserShortInfoSerializer


class FollowUpListSerializer(serializers.ModelSerializer):
    accident_date = serializers.DateField(source='case.accident_date', allow_null=True, required=False)
    client_name = serializers.CharField(source='case.client.name', allow_null=True, required=False)
    client_vehicle_vrn = serializers.CharField(source='case.client.vehicle.vrn', allow_null=True, required=False)
    client_vehicle_make_model = serializers.CharField(source='case.client.vehicle.make_model', allow_null=True, required=False)
    client_insurer_id = serializers.CharField(source='case.client.insurer', allow_null=True, required=False)
    user = UserShortInfoSerializer(required=False, allow_null=True)

    class Meta:
        model = FollowUp
        fields = (
            'id', 'case', 'date', 'communication', 'accident_date', 'client_name', 'client_vehicle_vrn',
            'client_vehicle_make_model', 'is_resolved', 'title', 'user', 'title_label', 'created_at',
            'client_insurer_id'
        )
