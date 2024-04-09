from django.contrib import admin

from parties.models import Insurer


@admin.register(Insurer)
class InsurerAdmin(admin.ModelAdmin):
    pass
