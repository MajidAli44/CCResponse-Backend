from django.contrib import admin

from core.models import Injury


@admin.register(Injury)
class InjuryAdmin(admin.ModelAdmin):
    pass
