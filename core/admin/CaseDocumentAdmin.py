from django.contrib import admin

from core.models import CaseDocument


@admin.register(CaseDocument)
class CaseDocumentAdmin(admin.ModelAdmin):
    pass
