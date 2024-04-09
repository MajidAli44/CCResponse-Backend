from django.db import models

from common.models import BaseAbstractModel


class AbstractExternalParty(BaseAbstractModel):
    name = models.CharField(max_length=255, blank=True, null=True, db_index=True)

    class Meta:
        abstract = True
