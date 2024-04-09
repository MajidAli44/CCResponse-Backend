from django.db import models

from common.models import BaseAbstractModel


class RepairInvoiceItem(BaseAbstractModel):

    name = models.CharField(max_length=128)
    price = models.DecimalField(decimal_places=2, max_digits=12)

