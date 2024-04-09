from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Case
from core.serializers import InvoiceSerializer


class CaseFinancialsAPIView(APIView):

    def get(self, request, *args, pk=None, **kwargs):
        case = get_object_or_404(Case.objects.get_queryset(), pk=pk)
        invoices_data = InvoiceSerializer(case.invoices.all().order_by('created_at'), many=True).data

        total_net = sum([
            invoice_data['total_net'] and float(invoice_data['total_net']) or 0
            for invoice_data in invoices_data
        ])
        total_vat = sum([
            invoice_data['total_vat'] and float(invoice_data['total_vat']) or 0
            for invoice_data in invoices_data
        ])
        total = sum([
            invoice_data['total'] and float(invoice_data['total']) or 0
            for invoice_data in invoices_data
        ])
        global_settled = sum([
            invoice_data['settled_amount_total'] and float(invoice_data['settled_amount_total']) or 0
            for invoice_data in invoices_data
        ])

        data = {
            'invoices': invoices_data,
            'total_net': "%.2f" % total_net if total_net else None,
            'total_vat': "%.2f" % total_vat if total_vat else None,
            'total': "%.2f" % total if total else None,
            'global_settled': "%.2f" % global_settled if global_settled else None,
        }

        return Response(
            data, status=status.HTTP_200_OK
        )
