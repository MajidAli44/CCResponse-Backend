from django.contrib import admin

from core.models import Attachment


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    pass


admin.register(Attachment, AttachmentAdmin)
