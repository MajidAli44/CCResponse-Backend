from rest_framework.generics import UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from api.pagination import SmallLimitOffsetPagination
from vehicles.models import Expense
from vehicles.serializers import ExpenseSerializer
from vehicles.services import HireVehicleService

vehicle_service = HireVehicleService()


class ExpenseUpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = SmallLimitOffsetPagination
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
