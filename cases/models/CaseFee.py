from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from common.models import BaseAbstractModel


class CaseFee(BaseAbstractModel):

    class OutsourcedTo(DjangoChoices):
        spectra = ChoiceItem('spectra', 'Spectra')
        winn = ChoiceItem('winn', 'WINN')
        blackthorn = ChoiceItem('blackthorn', 'Blackthorn')
        dwa = ChoiceItem('dwa', 'DWA')

    class RepairableStatus(DjangoChoices):
        repairable = ChoiceItem('repairable', 'Repairable')
        total_loss = ChoiceItem('total_loss', 'Total loss')

    class HireRefFee(DjangoChoices):
        fee_na = ChoiceItem('na', 'N/A')
        fee_450 = ChoiceItem('450', '£450')
        fee_500 = ChoiceItem('500', '£500')
        fee_750 = ChoiceItem('750', '£750')

    class SoldVia(DjangoChoices):
        copart = ChoiceItem('copart', 'Copart')
        ebay = ChoiceItem('ebay', 'Ebay')
        other = ChoiceItem('other', 'Other')

    outsourced_to = models.CharField(choices=OutsourcedTo.choices, max_length=32, blank=True, null=True)
    repair_status = models.CharField(choices=RepairableStatus.choices, max_length=32, blank=True, null=True)
    hire_ref_fee = models.CharField(choices=HireRefFee.choices, max_length=3, blank=True, null=True)
    repair_ref_fee = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)

    salvage_value = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    sold_via = models.CharField(choices=SoldVia.choices, max_length=16, blank=True, null=True)
    sale_price = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
