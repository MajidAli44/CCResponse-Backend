from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from invoices.models import Invoice
from invoices.serializers import InvoiceSerializer


class InvoiceUpdateAPIView(UpdateAPIView):
    lookup_url_kwarg = 'invoice_pk'
    permission_classes = (IsAuthenticated,)
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    http_method_names = ['patch']
