from django.db import models

from common.models import BaseAbstractModel


class HireValidation(BaseAbstractModel):
    engs_instructed = models.DateField(blank=True, null=True)
    inspection_date = models.DateField(blank=True, null=True)
    report_received = models.DateField(blank=True, null=True)
    sent_to_tp = models.DateField(blank=True, null=True)
    repairable = models.BooleanField(default=False)
    total_loss_cil = models.BooleanField(default=False)
    repair_auth = models.DateField(blank=True, null=True)
    sat_note_sign = models.DateField(blank=True, null=True)
    settle_offer = models.DateField(blank=True, null=True)
    offer_accepted = models.DateField(blank=True, null=True)
    cheque_received = models.DateField(blank=True, null=True)
    liability_admitted = models.BooleanField(blank=True, null=True)
    liability_admitted_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Hire validation'
        verbose_name_plural = 'Hire validations'
