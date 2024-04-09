from django.db import models

from .HireVehicle import HireVehicle


class Expense(models.Model):
    hire_vehicle = models.ForeignKey(
        HireVehicle, on_delete=models.CASCADE, related_name='expenses'
    )
    expense_date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True,
    )
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
