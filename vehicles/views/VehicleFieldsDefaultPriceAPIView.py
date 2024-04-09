from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from vehicles.models import VehicleFieldsDefaultPrice
from vehicles.serializers import VehicleFieldsDefaultPriceSerializer
from vehicles.services import HireVehicleService

vehicle_service = HireVehicleService()


class VehicleFieldsDefaultPriceAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = VehicleFieldsDefaultPriceSerializer

    def get_object(self):
        return VehicleFieldsDefaultPrice.objects.last()
