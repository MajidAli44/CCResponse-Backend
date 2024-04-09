from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from api.pagination import SmallLimitOffsetPagination
from notification.models import Notification
from notification.serializers import UnreadedNotificationSerializer


class UnreadedNotificationView(ListAPIView):

    permission_classes = (IsAuthenticated, )
    serializer_class = UnreadedNotificationSerializer
    pagination_class = SmallLimitOffsetPagination

    def get_queryset(self):
        return Notification.objects.filter()

    @swagger_auto_schema(operation_summary='List of notifications')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(user=request.user).order_by('-created_at')
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        response = self.get_paginated_response(serializer.data)

        unreaded = sum(1 if not current_notification.is_read else 0 for current_notification in queryset)
        response.data['unreaded'] = unreaded
        return response
