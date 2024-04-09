from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from notification.models import Notification


class NotificationReadAllByCaseIDView(APIView):

    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(operation_summary='Mark all case notification as read')
    def post(self, request, *args, **kwargs):
        case_id = kwargs.get('case_id')
        notifications = Notification.objects.filter(case=case_id, user=request.user)
        print("notification is---",notifications)
        if len(notifications) > 0:
            for notification in notifications:
                print("notification ID--",notification.id)
                notification.is_read = True
                notification.save()
        return JsonResponse({"status": True, "actions": "marked"})
