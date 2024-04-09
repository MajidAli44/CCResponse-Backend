from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from common.models import BaseAbstractModel
from core.models import User

from .Case import Case


class CaseNote(BaseAbstractModel):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='user_notes'
    )
    case = models.ForeignKey(
        Case, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='case_notes'
    )
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
