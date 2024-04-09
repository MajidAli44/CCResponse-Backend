from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from reports.models import Report
from core.permissions import IsCRMAdminUser
from reports.serializers import ReportSerializer


class ReportListCreateAPIView(ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticated, IsCRMAdminUser, )

    def perform_create(self, serializer):
        serializer.save()
