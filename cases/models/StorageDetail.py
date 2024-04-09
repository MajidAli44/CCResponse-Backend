from datetime import timedelta
from decimal import Decimal

from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from common.models import BaseAbstractModel


class StorageDetail(BaseAbstractModel):
    class StorageProvider(DjangoChoices):
        cc_response = ChoiceItem('cc_response', 'CC Response')
        copart = ChoiceItem('copart', 'Copart')

    class StorageStatus(DjangoChoices):
        pending = ChoiceItem('pending', 'Pending')
        pickup = ChoiceItem('pickup', 'Pickup')
        arranged = ChoiceItem('arranged', 'Arranged')

    """Model for storage detail of case"""
    from_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    fee_per_day = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True,
    )
    engineers_fee = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True,
    )
    provider = models.CharField(choices=StorageProvider.choices, max_length=20, blank=True, null=True)
    status = models.CharField(choices=StorageStatus.choices, max_length=20, blank=True, null=True)
    provider_ref = models.CharField(max_length=255, blank=True, null=True)

    @property
    def storage_total_sum(self):
        return (Decimal(self.days_in_storage) * (self.fee_per_day or Decimal('0.0'))).quantize(Decimal('1.00'))

    @property
    def days_in_storage(self):
        if self.from_date and self.end_date:
            return (self.end_date - self.from_date + timedelta(days=1)).days
        return 0

    def get_storage_total_fee(self):
        return (((self.days_in_storage or Decimal('0.0')) * (self.fee_per_day or Decimal('0.0'))) + (
                    self.engineers_fee or Decimal(
                "0.0")))

    @property
    def formatted_provider(self):
        return self.StorageProvider.get_choice(self.provider).label.split(' ')[0].upper()
