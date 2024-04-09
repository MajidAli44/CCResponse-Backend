from django.db import models

from common.models import BaseAbstractModel


class ClawbackDetail(BaseAbstractModel):
    """Model for clawback detail of case"""
    date = models.DateField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    replace_name = models.CharField(max_length=127, blank=True, null=True)
    intro_rep_case = models.DateField(blank=True, null=True)
    we_rep_case = models.DateField(blank=True, null=True)
    chase_date = models.DateField(blank=True, null=True)
    replaced = models.BooleanField(default=False)
