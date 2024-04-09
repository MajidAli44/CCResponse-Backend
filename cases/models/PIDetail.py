from django.db import models
from django.db.models import Sum
from djchoices import DjangoChoices, ChoiceItem

from common.models import BaseAbstractModel
from parties.models import Solicitor


class PIDetail(BaseAbstractModel):
    class Statuses(DjangoChoices):
        new = ChoiceItem('new', 'New')
        accepted = ChoiceItem('accepted', 'Accepted')
        rejected = ChoiceItem('rejected', 'Rejected')

    class ClaimTypes(DjangoChoices):
        rta = ChoiceItem('rta', 'RTA')
        aaw = ChoiceItem('aaw', 'AAW')
        ol = ChoiceItem('ol', 'OL')
        pl = ChoiceItem('pl', 'PL')

    class PiProviders(DjangoChoices):
        winn = ChoiceItem('winn', 'WINN')
        easidrive = ChoiceItem('easidrive', 'Easidrive')
        dgm = ChoiceItem('dgm', 'DGM')
        thompsons = ChoiceItem('thompsons', 'Thompsons')

    class PiStatus(DjangoChoices):
        pending = ChoiceItem('pending', 'Pending')
        accepted = ChoiceItem('accepted', 'Accepted')
        paid = ChoiceItem('paid', 'Paid')

    claim_type = models.CharField(
        choices=ClaimTypes.choices, max_length=50, blank=True, null=True
    )
    claim_num = models.PositiveIntegerField(blank=True, null=True)

    solicitor_introduced = models.ForeignKey(
        Solicitor, on_delete=models.SET_NULL, blank=True, null=True
    )
    instructed_paid_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=50, choices=Statuses.choices, default=Statuses.new
    )
    notes = models.TextField(blank=True, null=True)
    provider = models.CharField(choices=PiProviders.choices, blank=True, null=True, max_length=20)
    pi_status = models.CharField(choices=PiStatus.choices, blank=True, null=True, max_length=20)

    @property
    def pi_fee(self):
        total = self.piclient_set.all().aggregate(Sum('fee'))['fee__sum']
        if total is not None:
            return total
        return 0

    @property
    def formatted_provider(self):
        return self.PiProviders.get_choice(self.provider).label.split(' ')[0].upper()
