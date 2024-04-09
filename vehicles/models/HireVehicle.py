from django.db import models

from .AbstractVehicle import AbstractVehicle


class HireVehicle(AbstractVehicle):
    registration = models.CharField(max_length=127, blank=True, null=True, db_index=True)
    date_purchased = models.DateField(blank=True, null=True, db_index=True)
    purchase_price = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True, db_index=True
    )
    service_due = models.DateField(blank=True, null=True, db_index=True)
    tax_cost = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True, db_index=True
    )
    mot_cost = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True, db_index=True
    )
    notes = models.TextField(blank=True, null=True, db_index=True)
    is_sold = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Hire vehicle'
        verbose_name_plural = 'Hire vehicles'

    @property
    def last_hire_case(self):
        return self.hire_details.order_by('created_at').last()
