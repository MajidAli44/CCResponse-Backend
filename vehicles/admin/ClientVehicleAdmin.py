from django.contrib import admin

from vehicles.models import ClientVehicle


@admin.register(ClientVehicle)
class ClientVehicleAdmin(admin.ModelAdmin):
    pass
