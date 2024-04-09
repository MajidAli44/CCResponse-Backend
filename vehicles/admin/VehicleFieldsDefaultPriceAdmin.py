from django.contrib import admin

from vehicles.models import VehicleFieldsDefaultPrice


@admin.register(VehicleFieldsDefaultPrice)
class VehicleFieldsDefaultPriceAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if VehicleFieldsDefaultPrice.objects.all().count() > 0:
            return False
        return (
            super(VehicleFieldsDefaultPriceAdmin, self)
            .has_add_permission(request)
        )
