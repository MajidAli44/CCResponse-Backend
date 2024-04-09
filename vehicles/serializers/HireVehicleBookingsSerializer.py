from vehicles.models import HireVehicle
from .HireVehicleListSerializer import HireVehicleListSerializer


class HireVehicleBookingsSerializer(HireVehicleListSerializer):

    class Meta:
        model = HireVehicle
        fields = ('client_name', 'case_id', 'booking_from_to')

    def get_client_name(self, obj):
        try:
            return obj.case.client.name
        except AttributeError:
            return None

    def get_case_id(self, obj):
        try:
            return obj.case.id
        except AttributeError:
            return None

    def get_booking_from_to(self, obj):
        booking_from = obj.start_date
        booking_to = obj.end_date
        return {
            'booking_from': booking_from,
            'booking_to': booking_to
        }
