from django.urls import path, include

from invoices.views import InvoiceFileListAPIView

urlpatterns = [
    path('cases/', include('cases.urls')),
    path('parties/', include('parties.urls')),
    path('vehicles/', include('vehicles.urls')),
    path('documents/', include('documents.urls')),
    path('chat/', include('chat.urls')),
    path('notifications/', include('notification.urls')),
    path('invoices/', InvoiceFileListAPIView.as_view()),
    path('reports/', include('reports.urls')),
]
