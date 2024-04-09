from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.pagination import SmallLimitOffsetPagination
from invoices.models import Invoice
from invoices.serializers import InvoiceSerializer


class InvoiceListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = InvoiceSerializer
    pagination_class = SmallLimitOffsetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            grand_total = {
                'total_net': sum((invoice.total_net or 0) for invoice in queryset),
                'total_vat': sum((invoice.total_vat or 0) for invoice in queryset),
                'total': sum((invoice.total or 0) for invoice in queryset),
                'settlement_fee': sum((invoice.settlement_fee or 0) for invoice in queryset),
            }
            serializer = self.get_serializer(page, many=True)
            paginated_response = self.get_paginated_response(serializer.data)
            paginated_response.data['grand_total'] = grand_total
            return paginated_response

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return Invoice.objects.filter(case_id=self.kwargs.get('case_pk')).order_by('charge_type')
