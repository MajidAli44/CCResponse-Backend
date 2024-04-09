from django.db import models

from vehicles.models import ClientVehicle
from .AbstractParty import AbstractParty


class Client(AbstractParty):
    date_of_birth = models.CharField(blank=True, null=True, max_length=50)
    license_number = models.CharField(
        max_length=50, blank=True, null=True,
    )
    ni_number = models.CharField(max_length=100, blank=True, null=True)
    insurer = models.ForeignKey(
        'Insurer', on_delete=models.SET_NULL, blank=True, null=True,
        related_name='clients'
    )
    vehicle = models.ForeignKey(
        ClientVehicle, blank=True, null=True, on_delete=models.SET_NULL,
        related_name='client'
    )

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
