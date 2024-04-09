from django.contrib import admin

from core.models import Attachment


class AttachmentInline(admin.TabularInline):
    model = Attachment
