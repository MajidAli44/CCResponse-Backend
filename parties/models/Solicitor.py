from django.db import models

from.AbstractExternalParty import AbstractExternalParty


class Solicitor(AbstractExternalParty):
    fullname = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    hotkey_number = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    contact_number = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    pi_fee = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True, db_index=True)
    address = models.TextField(blank=True, null=True, db_index=True)
    notes = models.TextField(blank=True, null=True, db_index=True)

    class Meta:
        verbose_name = 'Solicitor'
        verbose_name_plural = 'Solicitors'
