from decimal import Decimal

from django.db import models
from django.db.models import Sum

from common.models import BaseAbstractModel
from invoices.models import RepairInvoiceItem


class RepairInvoice(BaseAbstractModel):
    labour_hours = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=12)
    labour_rate = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=12)

    paint_and_sundries = models.DecimalField(blank=True, null=True, default=Decimal(0), decimal_places=2, max_digits=12)
    parts_mlp = models.DecimalField(blank=True, null=True, default=Decimal(0), decimal_places=2, max_digits=12)
    remove_and_refit_glass = models.DecimalField(blank=True, null=True, default=Decimal(0), decimal_places=2,
                                                 max_digits=12)
    covid_clean_and_ppe = models.DecimalField(blank=True, null=True, default=Decimal(0), decimal_places=2,
                                              max_digits=12)
    specialist_1 = models.DecimalField(blank=True, null=True, default=Decimal(0), decimal_places=2, max_digits=12)
    miscellaneous_1 = models.DecimalField(blank=True, null=True, default=Decimal(0), decimal_places=2, max_digits=12)
    car_kit_and_mini_valet = models.DecimalField(blank=True, null=True, default=Decimal(0), decimal_places=2,
                                                 max_digits=12)
    geometry = models.DecimalField(blank=True, null=True, default=Decimal(0), decimal_places=2, max_digits=12)
    anti_corrosion = models.DecimalField(blank=True, null=True, default=Decimal(0), decimal_places=2, max_digits=12)
    epa = models.DecimalField(blank=True, null=True, default=Decimal(0), decimal_places=2, max_digits=12)

    items = models.ManyToManyField(RepairInvoiceItem)

    @property
    def repair_invoice_total(self):
        total = Decimal('0.0')
        labour_rate_total = (self.labour_hours or Decimal('0.0')) * (
                self.labour_rate or Decimal('0.0'))

        total += (labour_rate_total or Decimal('0.0')) + (
                self.paint_and_sundries or Decimal('0.0')) + (
                         self.parts_mlp or Decimal('0.0')) + (
                         self.remove_and_refit_glass or Decimal('0.0')) + (
                         self.covid_clean_and_ppe or Decimal('0.0')) + (
                         self.specialist_1 or Decimal('0.0')) + (
                         self.miscellaneous_1 or Decimal('0.0')) + (
                         self.car_kit_and_mini_valet or Decimal('0.0')) + (
                         self.geometry or Decimal('0.0')) + (
                         self.anti_corrosion or Decimal('0.0')) + (
                         self.epa or Decimal('0.0'))

        return total

    @property
    def total_repair_fee(self):
        total = self.items.all().aggregate(Sum('price'))['price__sum']
        if total is None:
            return 0
        return total
