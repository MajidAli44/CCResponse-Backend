from django.urls import path
from rest_framework import routers

from reports.views import ReportListCreateAPIView, ReportRetreiveUpdateDestroyAPIView

router = routers.SimpleRouter()

urlpatterns = [
    path('', ReportListCreateAPIView.as_view(), name='report_list_create'),
    path('<int:report_id>/', ReportRetreiveUpdateDestroyAPIView.as_view(), name='report_retreive_update_destroy'),
]

urlpatterns += router.urls
