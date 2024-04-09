from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from api.pagination import SmallLimitOffsetPagination
from vehicles.filters import VehicleFilter, CustomVehicleOrdering
from vehicles.models import HireVehicle
from vehicles.serializers import HireVehicleDetailSerializer, HireVehicleListSerializer
from vehicles.services import HireVehicleService

vehicle_service = HireVehicleService()


class VehicleListCreateAPIView(ListCreateAPIView):
    queryset = HireVehicle.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = SmallLimitOffsetPagination
    filter_backends = (
        SearchFilter, CustomVehicleOrdering, DjangoFilterBackend,
    )
    filterset_class = VehicleFilter
    search_fields = (
        'registration', 'hire_details__case__client__name',
        'make_model', 'mot_expiry', 'tax_expiry', 'service_due'
    )
    ordering_fields = (
        'registration', 'hire_details__case__client__name',
        'make_model', 'hire_details__case__start_date', 'mot_expiry',
        'tax_expiry', 'service_due'
    )

    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)
        response.data.update(
            **vehicle_service.get_each_status_count_of_vehicles()
        )
        return response

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'GET':
            return HireVehicleListSerializer
        return HireVehicleDetailSerializer
