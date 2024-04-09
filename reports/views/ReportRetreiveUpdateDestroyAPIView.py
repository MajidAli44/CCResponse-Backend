from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from reports.models import Report
from core.permissions import IsCRMAdminUser
from reports.serializers import ReportSerializer


class ReportRetreiveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'report_id'
    queryset = Report.objects.all()
    permission_classes = (IsAuthenticated, IsCRMAdminUser,)
    serializer_class = ReportSerializer
