from django.contrib import admin

from vehicles.models import ThirdPartyVehicle


@admin.register(ThirdPartyVehicle)
class ThirdPartyVehicleAdmin(admin.ModelAdmin):
    pass
