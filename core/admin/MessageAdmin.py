from django.contrib import admin

from core.admin.inlines import AttachmentInline
from core.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    inlines = [AttachmentInline]
