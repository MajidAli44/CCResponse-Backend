from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from core.models import Case, ExternalParty


class Injury(models.Model):
    class Type(DjangoChoices):
        rta = ChoiceItem('rta', 'RTA')
        trip_slip = ChoiceItem('trip_slip', 'Trip Slip')
        aaw = ChoiceItem('aaw', 'AAW')

    class Status(DjangoChoices):
        need_to_hotkey = ChoiceItem('need_to_hotkey', 'Need to hotkey')
        hotkeyed = ChoiceItem('hotkeyed', 'Hotkeyed')
        paid_also = ChoiceItem('paid_also', 'Paid Also')

    case = models.ForeignKey(Case, on_delete=models.SET_NULL, related_name='injuries', null=True)
    solicitor = models.ForeignKey(ExternalParty, on_delete=models.SET_NULL, related_name='injuries', null=True)
    date = models.DateField()
    type = models.CharField(max_length=15, choices=Type.choices)
    status = models.CharField(max_length=15, choices=Status.choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        custom_string = f'injury on {self.created_at.strftime("%b %d %Y %H:%M:%S")}'
        if self.solicitor:
            return f'{self.solicitor}\'s {custom_string}'
        else:
            return f'Solicitor {custom_string}'

    class Meta:
        verbose_name_plural = 'Injuries'
