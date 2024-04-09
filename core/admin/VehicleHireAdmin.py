from django.contrib import admin

from core.admin.forms import VehicleHireAdminForm
from core.models import VehicleHire


@admin.register(VehicleHire)
class VehicleHireAdmin(admin.ModelAdmin):
    form = VehicleHireAdminForm
