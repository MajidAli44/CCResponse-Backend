import datetime

from django.db import models
from django.db.models import Q
from djchoices import DjangoChoices, ChoiceItem


class Vehicle(models.Model):
    class Owner(DjangoChoices):
        customer = ChoiceItem('customer', 'Customer')
        third_party = ChoiceItem('third_party', 'Third Party')
        company = ChoiceItem('company', 'Company')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    vrn = models.CharField(max_length=100)
    make = models.CharField(max_length=200, blank=True)
    model = models.CharField(max_length=200, blank=True)
    date_purchased = models.DateField(blank=True, null=True)
    price_purchased = models.DecimalField(decimal_places=2, max_digits=15, blank=True, null=True)
    service_due = models.DateField(blank=True, null=True)
    tax_cost = models.DecimalField(decimal_places=2, max_digits=15, blank=True, null=True)
    tax_due = models.DateField(blank=True, null=True)
    mot_cost = models.DecimalField(decimal_places=2, max_digits=15, blank=True, null=True)
    mot_due = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    owner = models.CharField(choices=Owner.choices, default=Owner.company, max_length=20, db_index=True)
    is_sold = models.BooleanField(default=False)
    daily_hire_rate = models.DecimalField(decimal_places=2, max_digits=15)
    daily_storage_rate = models.DecimalField(decimal_places=2, max_digits=15, default=25)

    def __str__(self):
        if self.vrn and self.make and self.model:
            return f'{self.vrn} - {self.make} - {self.model}'
        return f'Vehicle with id = {self.pk}'

    @property
    def is_booked(self):
        return self.owner == self.Owner.company and self.vehicle_hires.filter(
            Q(end_date__isnull=True) | Q(end_date__gte=datetime.date.today()),
            start_date__lte=datetime.date.today()
        ).exists()
