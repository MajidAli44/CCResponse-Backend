from django.contrib import admin

from core.admin.inlines import ExpenseInline
from core.models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    inlines = [ExpenseInline]
