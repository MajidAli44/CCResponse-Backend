from django.contrib import admin

from core.admin.inlines import MessageInline
from core.models import Chat


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    inlines = [MessageInline]
