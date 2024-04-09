from django.contrib import admin

from cases.models import Case


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    pass
