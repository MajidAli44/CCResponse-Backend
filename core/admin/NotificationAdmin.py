from django.contrib import admin

from core.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass
