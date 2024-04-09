from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from vehicles.models import HireVehicle
from vehicles.serializers import HireVehicleDetailSerializer


class VehicleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = HireVehicle.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = HireVehicleDetailSerializer
