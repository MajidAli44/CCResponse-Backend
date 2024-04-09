from django.db import models

from vehicles.models import ThirdPartyVehicle
from .AbstractParty import AbstractParty


class ThirdParty(AbstractParty):
    policy_number = models.CharField(max_length=200, blank=True, null=True)
    other_details = models.TextField(blank=True, null=True)
    insurer = models.ForeignKey(
        'Insurer', on_delete=models.SET_NULL, blank=True, null=True,
        related_name='third_parties'
    )
    insurer_email = models.CharField(max_length=255, blank=True, null=True)
    insurer_contact_number = models.CharField(max_length=50, blank=True, null=True)
    insurer_ref = models.CharField(max_length=255, blank=True, null=True)
    vehicle = models.ForeignKey(
        ThirdPartyVehicle, blank=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = 'Third party'
        verbose_name_plural = 'Third parties'

