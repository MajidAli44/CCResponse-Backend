from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.pagination import SmallLimitOffsetPagination
from cases.models import HireDetail
from vehicles.models import HireVehicle
from vehicles.serializers import HireVehicleBookingsSerializer
from vehicles.services import HireVehicleService

vehicle_service = HireVehicleService()


class VehicleBookingsAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = SmallLimitOffsetPagination
    serializer_class = HireVehicleBookingsSerializer
    queryset = HireVehicle.objects.all()

    def get(self, request, *args, **kwargs):
        bookings = HireDetail.objects.filter(vehicle=self.get_object(), case__isnull=False)
        page = self.paginate_queryset(bookings)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(self.serializer_class(bookings, many=True).data)
