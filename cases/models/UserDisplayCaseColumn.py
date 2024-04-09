from django.contrib.postgres.fields import ArrayField
from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from core.models import User


class UserDisplayCaseColumn(models.Model):
    class CaseColumns(DjangoChoices):
        cc_ref = ChoiceItem('cc_ref', 'CC Ref')
        instruction_date = ChoiceItem('instruction_date', 'Instruction date')
        accident_date = ChoiceItem('accident_date', 'Accident date')
        client_name = ChoiceItem('client_name', 'Client name')
        phone_number = ChoiceItem('phone_number', 'Phone number')
        introducer = ChoiceItem('introducer', 'Introducer')
        provider = ChoiceItem('provider', 'Provider')
        instructed_solicitor = ChoiceItem('instructed_solicitor', 'Instructed solicitor')
        tp_insurer = ChoiceItem('tp_insurer', 'Third party insurer')
        status = ChoiceItem('status', 'Status')
        notes = ChoiceItem('notes', 'Notes')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    columns = ArrayField(
        models.CharField(max_length=20, choices=CaseColumns.choices),
        default=list, size=99
    )
