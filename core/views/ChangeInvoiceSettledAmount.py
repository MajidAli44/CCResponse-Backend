from decimal import Decimal as D

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Invoice
from core.serializers import InvoiceSerializer


class ChangeInvoiceSettledAmount(APIView):

    def post(self, request, *args, pk=None, **kwargs):
        invoice = get_object_or_404(Invoice.objects.get_queryset(), pk=pk)
        settled_amount_net = request.data.get('settled_amount_net', None)
        settled_amount_vat = request.data.get('settled_amount_vat', None)
        settled_amount_total = request.data.get('settled_amount_total', None)
        try:
            assert settled_amount_net
            settled_amount_net = float(settled_amount_net)
            settled_amount_vat = settled_amount_vat and float(settled_amount_vat)
            settled_amount_total = settled_amount_total and float(settled_amount_total)
        except (AssertionError, ValueError, TypeError):
            return Response(
                'Wrong amount format or settled_amount_net was not specified',
                status=status.HTTP_400_BAD_REQUEST
            )

        settled_amount_vat = settled_amount_vat or settled_amount_net * 0.2
        settled_amount_total = settled_amount_total or (settled_amount_net + settled_amount_vat)
        invoice.settled_amount_net = D(settled_amount_net)
        invoice.settled_amount_vat = D(settled_amount_vat)
        invoice.settled_amount_total = D(settled_amount_total)
        invoice.save()

        return Response(InvoiceSerializer(invoice).data, status=status.HTTP_200_OK)
