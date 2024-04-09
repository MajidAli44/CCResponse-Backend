from django.contrib import admin

from core.models import Message

class MessageInline(admin.TabularInline):
    model = Message
