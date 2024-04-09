from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from notification.models import Notification


class NotificationReadAllView(APIView):

    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(operation_summary='Mark all user notification as read')
    def post(self, request, *args, **kwargs):
        Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
        return JsonResponse({"status": True, "actions": "marked"})
