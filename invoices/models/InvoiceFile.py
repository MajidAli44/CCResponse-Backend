from decimal import Decimal

from django.db import models

from cases.models import Case
from common.models import BaseAbstractModel


class InvoiceFile(BaseAbstractModel):

    case = models.ForeignKey(Case, on_delete=models.SET_NULL, related_name='invoice_files', null=True)

    hire_invoice_date = models.DateField(blank=True, null=True)
    hire_invoice_total = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)

    storage_invoice_date = models.DateField(blank=True, null=True)
    storage_invoice_total = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)

    recovery_invoice_date = models.DateField(blank=True, null=True)
    recovery_invoice_total = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)

    last_invoice_date = models.DateField(blank=True, null=True)

    def invoice_count(self):
        count = 0

        if self.hire_invoice_total is not None and self.hire_invoice_date is not None:
            count += 1
        if self.storage_invoice_total is not None and self.storage_invoice_date is not None:
            count += 1
        if self.recovery_invoice_total is not None and self.recovery_invoice_total is not None:
            count += 1

        return count

    def total(self):
        total = Decimal(0.00)
        total += Decimal(self.hire_invoice_total or '0.00')
        total += Decimal(self.storage_invoice_total or '0.00')
        total += Decimal(self.recovery_invoice_total or '0.00')
        return total.quantize(Decimal('0.00'))
