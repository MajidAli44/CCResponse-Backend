from decimal import Decimal

from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from cases.models import Case
from cases.services import CaseService
from common.models import BaseAbstractModel


class Invoice(BaseAbstractModel):
    class InvoiceType(DjangoChoices):
        hire = ChoiceItem('hire', 'Hire')
        storage_and_recovery = ChoiceItem('storage_and_recovery', 'Storage/Recovery')

    case = models.ForeignKey(Case, on_delete=models.SET_NULL, related_name='invoices', null=True)
    charge_type = models.CharField(max_length=20, choices=InvoiceType.choices, null=True)
    settlement_fee = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)

    @property
    def total_net(self):
        if self.charge_type == self.InvoiceType.storage_and_recovery:
            return CaseService.calculate_storage_total_net(self.case) if self.case else Decimal('0.0')
        return CaseService.calculate_hire_total_net(self.case) if self.case else Decimal('0.0')

    @property
    def total_vat(self):
        return self.total_net / 5

    @property
    def total(self):
        return self.total_net + self.total_vat

    def total_hire_fee(self):
        return CaseService.calculate_hire_total_net(self.case) if self.case else Decimal('0.0')

    def total_storage_fee(self):
        return CaseService.calculate_storage_total_net(self.case) if self.case else Decimal('0.0')
