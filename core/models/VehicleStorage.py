from django.db import models

from core.models import VehicleAction, Case, Vehicle, Customer


class VehicleStorage(VehicleAction):
    # Has One2One field related in Invoice
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, related_name='storages', blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, related_name='vehicle_storages', null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='customer_storages', null=True)
    daily_storage_rate = models.DecimalField(decimal_places=2, max_digits=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.daily_storage_rate and self.vehicle:
            self.daily_storage_rate = self.vehicle.daily_storage_rate
        super().save(*args, **kwargs)
