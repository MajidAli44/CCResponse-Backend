from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from cases.models import HireDetail
from cases.serializers import HireDetailDashboardSerializer
from django.utils import timezone

class CaseHireDetailCreateAPIView(ListCreateAPIView):
    queryset = HireDetail.objects.filter(end_date__gt=timezone.now(), case__isnull=False).order_by('end_date')
    serializer_class = HireDetailDashboardSerializer
    permission_classes = (IsAuthenticated,)

