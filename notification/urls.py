from django.urls import path

from notification.views import UnreadedNotificationView, NotificationReadView, NotificationReadAllView, \
    NotificationReadAllByCaseIDView

urlpatterns = [
    path('', UnreadedNotificationView.as_view(), name='unreaded_notifications'),
    path('notification/<int:notification_id>', NotificationReadView.as_view()),
    path('case/<int:case_id>', NotificationReadAllByCaseIDView.as_view()),
    path('all/', NotificationReadAllView.as_view())
]
