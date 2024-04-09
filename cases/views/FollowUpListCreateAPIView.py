from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from cases.filters import FollowupFilter
from cases.models import FollowUp
from cases.serializers import FollowUpListSerializer, FollowUpCreateSerializer


class FollowUpListCreateAPIView(ListCreateAPIView):
    lookup_url_kwarg = 'follow_up_pk'
    permission_classes = (IsAuthenticated,)
    queryset = FollowUp.objects.all()
    filter_backends = (
        filters.SearchFilter, DjangoFilterBackend
    )
    filterset_class = FollowupFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FollowUpListSerializer
        return FollowUpCreateSerializer


class FollowUpDashboardListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = FollowUp.objects.filter(is_resolved=False)
    filter_backends = (
        filters.SearchFilter, DjangoFilterBackend
    )
    filterset_class = FollowupFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FollowUpListSerializer
        return FollowUpCreateSerializer
