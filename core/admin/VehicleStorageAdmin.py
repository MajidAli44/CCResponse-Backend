from django.contrib import admin

from core.admin.forms import VehicleStorageAdminForm
from core.models import VehicleStorage


@admin.register(VehicleStorage)
class VehicleStorageAdmin(admin.ModelAdmin):
    form = VehicleStorageAdminForm
