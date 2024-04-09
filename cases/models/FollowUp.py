from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from common.models import BaseAbstractModel
from core.models import User
from .Case import Case


class FollowUp(BaseAbstractModel):
    class TypeChoices(DjangoChoices):
        follow_up = ChoiceItem('follow_up', 'Follow up')
        insurer_chase = ChoiceItem('insurer_chase', 'Insurer chase')
        client_update = ChoiceItem('client_update', 'Client update')

        liability_vd_chasers = ChoiceItem('liability_vd_chasers', 'Liability/VD Chasers')
        er_client_approval = ChoiceItem('er_client_approval', 'ER Client Approval')
        cases_in_validation = ChoiceItem('cases_in_validation', 'Cases in Validation')
        vehicle_collections = ChoiceItem('vehicle_collections', 'Vehicle Collections')
        general_follow_up = ChoiceItem('general_follow_up', 'General Follow Up')

    case = models.ForeignKey(
        Case, blank=True, null=True, on_delete=models.CASCADE,
        related_name='follow_ups'
    )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='user_tasks'
    )
    title = models.CharField(choices=TypeChoices.choices, max_length=55, default='follow_up')
    date = models.DateField(blank=True, null=True)
    communication = models.TextField(blank=True, null=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Follow Up'
        verbose_name_plural = 'Follow Ups'

    @property
    def title_label(self):
        return self.TypeChoices.get_choice(self.title).label
