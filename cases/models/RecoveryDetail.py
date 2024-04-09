from decimal import Decimal

from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from cases.models import CaseFieldsDefaultPrice
from common.models import BaseAbstractModel


class RecoveryDetail(BaseAbstractModel):
    class RecoveryTypes(DjangoChoices):
        standard = ChoiceItem('standard', 'Standard')
        out_of_hours = ChoiceItem('out_of_hours', 'Out of hours')
        would_not_drive_steer_roll = ChoiceItem('would_not_drive_steer_roll', 'Would not drive/Steer/Roll')
        crane_four_wheel_lift_required = ChoiceItem('crane_four_wheel_lift_required', 'Crane/Four wheel lift required')
        other = ChoiceItem('other', 'Other')

    class WinchingTimes(DjangoChoices):
        null = ChoiceItem('null', 'null')
        minutes_30 = ChoiceItem('minutes_30', '30 Minutes')
        hour_1 = ChoiceItem('hour_1', '1 Hour')

    class Skates(DjangoChoices):
        zero = ChoiceItem('zero', '0')
        one = ChoiceItem('one', '1')
        two = ChoiceItem('two', '2')
        three = ChoiceItem('three', '3')
        four = ChoiceItem('four', '4')
        five = ChoiceItem('five', '5')

    recovery_date = models.DateField(blank=True, null=True)
    recovery_type = models.CharField(choices=RecoveryTypes.choices, max_length=50, blank=True, null=True)
    other_recovery_reason = models.CharField(max_length=255, blank=True, null=True)
    call_out_charge = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    winching_time = models.CharField(choices=WinchingTimes.choices, max_length=50, blank=True, null=True)
    road_cleanup = models.BooleanField(default=False, blank=True, null=True)
    inherited_fees = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    skates = models.CharField(choices=Skates.choices, max_length=5, blank=True, null=True)

    @property
    def recovery_fee(self):
        recovery_fee = Decimal('0.0')

        recovery_fee += self.call_out_charge if self.call_out_charge is not None else Decimal(0.0)

        default_prices = CaseFieldsDefaultPrice.objects.first()

        if self.winching_time == RecoveryDetail.WinchingTimes.minutes_30:
            recovery_fee += default_prices.recovery_detail_minutes_30
        elif self.winching_time == RecoveryDetail.WinchingTimes.hour_1:
            recovery_fee += default_prices.recovery_detail_hour_1

        if self.road_cleanup:
            recovery_fee += default_prices.recovery_detail_road_cleanup

        if self.skates == RecoveryDetail.Skates.one:
            recovery_fee += default_prices.hire_detail_one_fee_for_skates
        elif self.skates == RecoveryDetail.Skates.two:
            recovery_fee += default_prices.hire_detail_one_fee_for_skates * 2
        elif self.skates == RecoveryDetail.Skates.three:
            recovery_fee += default_prices.hire_detail_one_fee_for_skates * 3
        elif self.skates == RecoveryDetail.Skates.four:
            recovery_fee += default_prices.hire_detail_one_fee_for_skates * 4
        elif self.skates == RecoveryDetail.Skates.five:
            recovery_fee += default_prices.hire_detail_one_fee_for_skates * 5

        recovery_fee += self.inherited_fees if self.inherited_fees is not None else Decimal(0.0)
        return recovery_fee
