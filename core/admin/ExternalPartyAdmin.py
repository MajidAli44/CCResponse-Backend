from django.contrib import admin

from core.models import ExternalParty


@admin.register(ExternalParty)
class ExternalPartyAdmin(admin.ModelAdmin):
    pass
