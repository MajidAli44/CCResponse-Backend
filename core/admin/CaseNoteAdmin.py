from django.contrib import admin

from core.models import CaseNote


@admin.register(CaseNote)
class CaseNoteAdmin(admin.ModelAdmin):
    pass
