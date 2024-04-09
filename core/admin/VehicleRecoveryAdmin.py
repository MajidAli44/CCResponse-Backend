from django.contrib import admin

from core.admin.forms import VehicleRecoveryAdminForm
from core.models import VehicleRecovery


@admin.register(VehicleRecovery)
class VehicleRecoveryAdmin(admin.ModelAdmin):
    form = VehicleRecoveryAdminForm
