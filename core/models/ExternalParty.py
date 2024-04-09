from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from core.models import Party


class ExternalParty(Party):
    class Role(DjangoChoices):
        insurer = ChoiceItem('insurer', 'Insurer')
        introducer = ChoiceItem('introducer', 'Introducer')
        solicitor = ChoiceItem('solicitor', 'Solicitor')

    role = models.CharField(max_length=50, choices=Role.choices)
    ref = models.CharField(max_length=200, blank=True)
    is_third_party = models.BooleanField(default=False)
    introducer_fee = models.DecimalField(decimal_places=2, max_digits=15, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'External parties'

    def __str__(self):
        return f'{self.role.title()} {self.name}'
