from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.pagination import SmallLimitOffsetPagination
from cases.models import Case
from invoices.filters import InvoiceFileFilter
from invoices.models import InvoiceFile
from invoices.serializers import InvoicesListSerializer


class InvoiceFileListAPIView(ListAPIView):

    queryset = Case.objects.all()
    serializer_class = InvoicesListSerializer
    pagination_class = SmallLimitOffsetPagination
    filter_backends = (DjangoFilterBackend, )
    filterset_class = InvoiceFileFilter

    def list(self, request, *args, **kwargs):
        settlement_status = self.request.query_params.get('settlement_status', None)
        cases = self.get_queryset()
        if settlement_status is not None:
            cases = cases.filter(status_description=settlement_status)
        cases = cases.only('pk')

        invoices = InvoiceFile.objects.filter(case__in=cases)

        page = self.paginate_queryset(invoices)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginated_response = self.get_paginated_response(serializer.data)
            return paginated_response

        serializer = self.get_serializer(invoices, many=True)
        return Response(serializer.data)
