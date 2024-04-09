from django.db import models

from .AbstractExternalParty import AbstractExternalParty


class Insurer(AbstractExternalParty):
    phone_number = models.CharField(max_length=127, blank=True, null=True, db_index=True)
    email = models.CharField(max_length=255, blank=True, null=True, db_index=True)

    class Meta:
        verbose_name = 'Insurer'
        verbose_name_plural = 'Insurers'
