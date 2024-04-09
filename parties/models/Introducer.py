from django.db import models

from .AbstractExternalParty import AbstractExternalParty


class Introducer(AbstractExternalParty):
    company_number = models.CharField(max_length=128, blank=True, null=True, db_index=True)
    contact_number = models.CharField(max_length=128, blank=True, null=True, db_index=True)
    office_number = models.CharField(max_length=128, blank=True, null=True, db_index=True)
    hire_fee = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, db_index=True)
    pi_fee = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, db_index=True)
    address = models.TextField(blank=True, null=True, db_index=True)

    class Meta:
        verbose_name = 'Introducer'
        verbose_name_plural = 'Introducers'
