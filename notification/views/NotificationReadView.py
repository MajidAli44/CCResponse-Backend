from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from notification.models import Notification


class NotificationReadView(APIView):

    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(operation_summary='Mark notification as read by ID')
    def post(self, request, *args, **kwargs):
        notification_id = kwargs.get('notification_id')
        print("requested User---", request.user)
        print("notification Id---", request.user)
        notification = Notification.objects.filter(id=notification_id, user=request.user)

        if len(notification) > 0:
            notification = notification[0]
            print("notification---",notification)
            notification.is_read = True
            notification.save()
            return JsonResponse({"status": True, "actions": "marked"})
        return JsonResponse({"status": False, "message": "not found"})
