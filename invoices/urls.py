from django.urls import path

from invoices.views import InvoiceListAPIView, InvoiceUpdateAPIView

urlpatterns = [
    path('', InvoiceListAPIView.as_view(), name='invoice_list'),
    path('<invoice_pk>/', InvoiceUpdateAPIView.as_view(), name='invoice_update'),
]
