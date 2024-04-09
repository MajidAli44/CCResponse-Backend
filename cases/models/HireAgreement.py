from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from common.models import BaseAbstractModel


class HireAgreement(BaseAbstractModel):

    class HireAgreementOfferReceivedStatuses(DjangoChoices):
        received = ChoiceItem('received', 'Received')
        not_received = ChoiceItem('not_received', 'Not received')

    offer_received = models.CharField(choices=HireAgreementOfferReceivedStatuses.choices, max_length=32, blank=True, null=True)

    personally_liable = models.BooleanField(default=False, blank=True, null=True)
    vehicle_unroadworthy = models.BooleanField(default=False, blank=True, null=True)
    no_another_vehicle = models.BooleanField(default=False, blank=True, null=True)

    prosecution = models.BooleanField(default=False, blank=True, null=True)
    accident_loss_in_3_past_years = models.BooleanField(default=False, blank=True, null=True)
    proposal_declined_or_increased_fees = models.BooleanField(default=False, blank=True, null=True)
    diseases = models.BooleanField(default=False, blank=True, null=True)


