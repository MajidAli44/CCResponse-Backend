from rest_framework import serializers

from vehicles.models import HireVehicle


class HireVehicleListSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()
    case_id = serializers.SerializerMethodField()
    booking_from_to = serializers.SerializerMethodField()

    class Meta:
        model = HireVehicle
        fields = (
            'id', 'make_model', 'mot_expiry', 'tax_expiry', 'registration',
            'service_due', 'client_name', 'booking_from_to', 'is_sold', 'case_id'
        )

    def get_client_name(self, obj):
        try:
            return obj.last_hire_case.case_set.last().client.name
        except AttributeError:
            return None

    def get_case_id(self, obj):
        try:
            return obj.last_hire_case.case_set.last().id
        except AttributeError:
            return None

    def get_booking_from_to(self, obj):
        last_hire_case = obj.last_hire_case
        if last_hire_case:
            booking_from = last_hire_case.start_date
            booking_to = last_hire_case.end_date
            return {
                'booking_from': booking_from,
                'booking_to': booking_to
            }
