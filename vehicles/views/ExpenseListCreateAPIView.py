from django.db.models import Sum, DecimalField
from django.db.models.functions import Coalesce
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from api.pagination import SmallLimitOffsetPagination
from vehicles.models import HireVehicle, Expense
from vehicles.serializers import ExpenseSerializer


class ExpenseListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = SmallLimitOffsetPagination
    serializer_class = ExpenseSerializer

    def _get_hire_vehicle(self):
        try:
            return HireVehicle.objects.get(id=self.kwargs.get('pk'))
        except HireVehicle.DoesNotExist:
            raise NotFound(detail={'detail': 'Hire vehicle not found'})

    def perform_create(self, serializer):
        serializer.validated_data['hire_vehicle'] = self._get_hire_vehicle()
        serializer.save()

    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)
        # get grand total and append to response data
        response.data.update(
            self._get_hire_vehicle().expenses
                .aggregate(grand_total=Coalesce(
                Sum('cost'), 0, output_field=DecimalField())
            )
        )
        return response

    def get_queryset(self):
        return Expense.objects.filter(hire_vehicle_id=self.kwargs.get('pk'))
