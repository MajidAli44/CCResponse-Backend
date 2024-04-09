from django.db import models

from core.models import VehicleAction, Case, Vehicle, Customer


class VehicleRecovery(VehicleAction):
    # Has One2One field related in Invoice
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, related_name='recoveries', blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, related_name='vehicle_recoveries', null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='customer_recoveries', null=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=15)
    recovery_type = models.CharField(max_length=50, null=True, blank=True)
    call_out_charge = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    winching_time = models.DateField(null=True, blank=True)
    road_cleanup = models.BooleanField(default=False)
    skates = models.BooleanField(default=False)
    inherited_fees = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    engineers_fee = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    date_repair_authorized = models.DateField(null=True, blank=True)
    date_satisfaction_note_signed = models.DateField(null=True, blank=True)
