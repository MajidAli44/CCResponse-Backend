from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from common.models import BaseAbstractModel


class Accident(BaseAbstractModel):
    """Model for accident of case"""

    class Circumstances(DjangoChoices):
        hir = ChoiceItem('hir', 'HIR')
        tp_pulled_from_sr = ChoiceItem('tp_pulled_from_sr', 'TP pulled from SR')
        roundabout_accident = ChoiceItem('roundabout_accident', 'Roundabout accident')
        lane_change = ChoiceItem('lane_change', 'Lane change')
        tp_pulled_from_parked_position = ChoiceItem('tp_pulled_from_parked_position', 'TP pulled from parked position')
        reversing_accident = ChoiceItem('reversing_accident', 'Reversing accident')
        car_park_accident = ChoiceItem('car_park_accident', 'Car park accident')
        other = ChoiceItem('other', 'Other')

    accident_date = models.DateField(blank=True, null=True)
    approx_time = models.CharField(max_length=32, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    circumstances = models.CharField(
        max_length=50, choices=Circumstances.choices, blank=True, null=True
    )
    weather = models.CharField(max_length=255, blank=True, null=True)
    other_info = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Accident'
        verbose_name_plural = 'Accidents'
