import datetime
from decimal import Decimal as D

from django.db import models

from core.models import VehicleAction, Case, Vehicle, Customer, Invoice, VehicleHireValidation


# pylint: disable=E1101
class VehicleHire(VehicleAction):
    # Has One2One field related in Invoice
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, related_name='hires', blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, related_name='vehicle_hires', null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='customer_hires', null=True)

    daily_hire_rate = models.DecimalField(decimal_places=2, max_digits=15, blank=True, null=True)
    start_hire_latitude = models.CharField(max_length=50, blank=True)
    start_hire_longitude = models.CharField(max_length=50, blank=True)
    end_hire_latitude = models.CharField(max_length=50, blank=True)
    end_hire_longitude = models.CharField(max_length=50, blank=True)

    # Fields used in case
    outsourced = models.BooleanField(default=False)
    clear_booking = models.BooleanField(default=False)

    collection = models.BooleanField(default=False)
    collection_cost = models.DecimalField(max_digits=15, decimal_places=2, default=D(50.00))

    delivery = models.BooleanField(default=False)
    delivery_cost = models.DecimalField(max_digits=15, decimal_places=2, default=D(50.00))

    cwd_required = models.BooleanField(default=False)
    cwd_per_day = models.DecimalField(max_digits=15, decimal_places=2, default=D(12.00))

    add_driver = models.BooleanField(default=False)
    driver_price = models.DecimalField(max_digits=15, decimal_places=2, default=D(5.00))

    sat_nav = models.BooleanField(default=False)
    sat_nav_price = models.DecimalField(max_digits=15, decimal_places=2, default=D(5.00))

    auto = models.BooleanField(default=False)
    auto_price = models.DecimalField(max_digits=15, decimal_places=2, default=D(5.00))

    towbar = models.BooleanField(default=False)
    towbar_price = models.DecimalField(max_digits=15, decimal_places=2, default=D(5.00))

    bluetooth = models.BooleanField(default=False)
    bluetooth_price = models.DecimalField(max_digits=15, decimal_places=2, default=D(5.00))

    ns_drive_charge = models.DecimalField(max_digits=15, decimal_places=2, default=D(0.00))

    def save(self, *args, **kwargs):
        if not self.daily_hire_rate and self.vehicle:
            self.daily_hire_rate = self.vehicle.daily_hire_rate

        try:
            if not self.case and self.invoice:
                self.case = self.invoice.case
        except Invoice.DoesNotExist:
            pass

        super().save(*args, **kwargs)

        if self.case is not None and self.end_date:
            Invoice.objects.update_or_create(
                case_id=self.case_id,
                vehicle_hire_id=self.pk,
                invoice_type=Invoice.InvoiceType.hire,
                defaults={
                    'invoice_number': 'INVOICE NUMBER',
                    'invoice_date': datetime.date.today()
                }
            )

        VehicleHireValidation.objects.get_or_create(vehicle_hire_id=self.pk)

    def __str__(self):
        custom_string = f'{self.customer} booked {self.vehicle} from {self.start_date.strftime("%b %d %Y")}'
        if self.end_date:
            custom_string += f'to {self.end_date.strftime("%b %d %Y")}'
        return custom_string
