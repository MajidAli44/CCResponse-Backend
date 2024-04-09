from django.contrib import admin

from cases.models import Accident


@admin.register(Accident)
class AccidentAdmin(admin.ModelAdmin):
    pass
