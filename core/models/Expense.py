from django.db import models

from core.models import Vehicle


class Expense(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, related_name='expenses', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(default='')
    cost = models.DecimalField(decimal_places=2, max_digits=15)
    date = models.DateField()

    def __str__(self):
        if self.vehicle:
            custom_string = self.vehicle.vrn
        else:
            custom_string = 'vehicle'
        return f'Expense for {custom_string} on {self.created_at.strftime("%b %d %Y %H:%M:%S")}'
