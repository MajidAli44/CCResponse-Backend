from django.db import models

from cases.models import PIDetail
from common.models import BaseAbstractModel


class PiClient(BaseAbstractModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    solicitor_ref = models.CharField(max_length=100, blank=True, null=True)
    fee = models.DecimalField(max_digits=12, decimal_places=2,  blank=True, null=True)
    pi_detail = models.ForeignKey(
        PIDetail, on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        verbose_name = 'PiClient'
        verbose_name_plural = 'PiClients'
