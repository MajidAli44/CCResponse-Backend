from decimal import Decimal

from django.db import models


class VehicleFieldsDefaultPrice(models.Model):
    """ Model for set vehicle default prices """
    hire_vehicle_purchase_price = models.DecimalField(
        decimal_places=2, max_digits=12, default=Decimal(0.0)
    )
    hire_vehicle_tax_cost = models.DecimalField(
        decimal_places=2, max_digits=12, default=Decimal(0.0)
    )
    hire_vehicle_mot_cost = models.DecimalField(
        decimal_places=2, max_digits=12, default=Decimal(0.0)
    )
    expense_cost = models.DecimalField(
        decimal_places=2, max_digits=12, default=Decimal(0.0)
    )

    class Meta:
        verbose_name = 'Vehicle fields default price'
