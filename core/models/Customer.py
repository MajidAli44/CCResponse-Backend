from django.db import models

from core.models import Party


class Customer(Party):
    date_of_birth = models.DateField(blank=True, null=True)
    license_number = models.CharField(max_length=100, blank=True)
    ni_number = models.CharField(max_length=100, blank=True)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, related_name='customers', null=True, blank=True)

    def __str__(self):
        return f'Customer {self.name}'
