from django.db.models import Sum
from django.db.models.fields import DecimalField
from django.db.models.functions import Coalesce
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Expense
from core.serializers import ExpenseSerializer
from core.utils import PaginatedQSMixin


class ExpensesViewSet(ModelViewSet, PaginatedQSMixin):
    serializer_class = ExpenseSerializer
    expense_fields = Expense.__dict__.copy()

    def get_queryset(self):
        return Expense.objects.get_queryset()

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()

        query_params = request.query_params.copy()

        (
            truncated_qs, count, _,
            old_query_params, page, page_size, total_aggregates_results
        ) = self.apply_query_params(
            query_params, qs, self.expense_fields,
            total_aggregates={'grand_total': Coalesce(Sum('cost'), 0, output_field=DecimalField())}
        )

        data = self.build_paginated_response_without_results(
            request, old_query_params, count, page, page_size, total_aggregates_results
        )

        data['results'] = self.get_serializer(truncated_qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
