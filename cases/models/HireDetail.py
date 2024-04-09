from datetime import timedelta
from decimal import Decimal

from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from common.models import BaseAbstractModel
from vehicles.models import HireVehicle


class HireDetail(BaseAbstractModel):
    """Model for hire detail of case"""

    class SettlementStatuses(DjangoChoices):
        with_cc_response = ChoiceItem('with_cc_response',
                                      'With CC Response')
        with_solicitor_stage_two = ChoiceItem('with_solicitor_stage_two',
                                              'With Solicitor - Stage 2')
        with_solicitor_issued = ChoiceItem('with_solicitor_issued',
                                           'With Solicitor - Issued')
        settlement_agreed = ChoiceItem('settlement_agreed',
                                       'Settlement Agreed')
        settlement_received = ChoiceItem('settlement_received',
                                         'Settlement Received')

    class NSDriverReason(DjangoChoices):
        age = ChoiceItem('age', 'Age (under 25 or older than 70)')
        occupation = ChoiceItem('occupation', 'Occupation')
        driving_licence = ChoiceItem('driving_licence', 'Held a full driving licence in the UK for less than 12 months')
        convictions_points = ChoiceItem('convictions_points', 'Convictions/points')

    # SERVICE PROVIDER FOR HIRE DETAILS

    class HireServiceProvider(DjangoChoices):
        ccr = ChoiceItem('ccr', 'CCR')
        europcar = ChoiceItem('europcar', 'Europcar')
        winn = ChoiceItem('winn', 'WINN')
        erac = ChoiceItem('erac', 'ERAC')
        spectra = ChoiceItem('spectra', 'Spectra')
        strada = ChoiceItem('strada', 'Strada')

    class HireStatus(DjangoChoices):
        hire_arranged = ChoiceItem('hire_arranged', 'Hire Arranged')
        in_hire = ChoiceItem('in_hire', 'In Hire')
        hire_ended = ChoiceItem('hire_ended', 'Hire ended')
        rejected = ChoiceItem('rejected', 'Rejected')

    class HireCategories(DjangoChoices):
        standard = ChoiceItem('standard', 'Standard')
        prestige = ChoiceItem('prestige', 'Prestige')
        taxi = ChoiceItem('taxi', 'Taxi')

    class OutsourcedVehicleFees(DjangoChoices):
        standard = ChoiceItem('400.00', 'Standard')
        prestige = ChoiceItem('650.00', 'Prestige')

    # Hire Details part
    # TODO: add model for hire detail
    vehicle = models.ForeignKey(
        HireVehicle, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='hire_details'
    )

    outsourced_vehicle = models.BooleanField(default=False)
    outsourced_vehicle_vrn = models.CharField(max_length=128, blank=True, null=True)
    outsourced_vehicle_make_model = models.CharField(max_length=128, blank=True, null=True)
    outsourced_vehicle_fee = models.CharField(choices=OutsourcedVehicleFees.choices, max_length=12, null=True,
                                              blank=True)

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    outsourced = models.BooleanField(default=False)
    charge = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    collection = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    delivery = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    cdw_required = models.BooleanField(default=False)
    cdw = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)

    driver_required = models.BooleanField(default=False)
    driver_full_name = models.CharField(max_length=128, blank=True, null=True)
    driver_date_of_birth = models.DateField(blank=True, null=True)
    driver_license_number = models.CharField(max_length=128, blank=True, null=True)
    driver_fee = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)

    sat_nav = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    auto = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    towbar = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    bluetooth = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)

    ns_driver_surcharge = models.BooleanField(default=False)
    ns_driver_fee = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    ns_driver_reason = models.CharField(choices=NSDriverReason.choices, max_length=18, blank=True, null=True)
    provider = models.CharField(choices=HireServiceProvider.choices, max_length=20, blank=True, null=True)
    status = models.CharField(choices=HireStatus.choices, max_length=20, blank=True, null=True)

    # Settlement Details part

    settlement_status = models.CharField(
        max_length=50, choices=SettlementStatuses, blank=True, null=True
    )
    hire_fee = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True,
    )
    recovery_fee = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True,
    )
    engineers_fee = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True,
    )
    storage_fee = models.DecimalField(
        decimal_places=2, max_digits=12, blank=True, null=True,
    )

    abi_cat = models.CharField(max_length=255, blank=True, null=True)
    hire_categories = models.CharField(choices=HireCategories.choices, max_length=20, blank=True, null=True)

    @property
    def due_back_date(self):
        if self.start_date:
            return (self.start_date + timedelta(days=89)).strftime("%d/%m/%Y")

    @property
    def days_in_hire(self):
        if self.start_date and self.end_date:
            return (self.end_date - self.start_date + timedelta(days=1)).days
        return 0

    @property
    def hire_fee_per_day(self):
        hire_fee_per_day = Decimal(0)
        hire_fee_per_day += self.charge or Decimal('0.00')

        hire_fee_per_day += self.collection or Decimal('0.00')
        hire_fee_per_day += self.delivery or Decimal('0.00')
        hire_fee_per_day += self.sat_nav or Decimal('0.00')
        hire_fee_per_day += self.auto or Decimal('0.00')
        hire_fee_per_day += self.bluetooth or Decimal('0.00')
        hire_fee_per_day += self.towbar or Decimal('0.00')

        if self.outsourced_vehicle_fee:
            hire_fee_per_day += Decimal(self.outsourced_vehicle_fee) or Decimal('0.00')

        if self.driver_required:
            hire_fee_per_day += self.driver_fee or Decimal('0.00')

        if self.cdw_required:
            hire_fee_per_day += self.cdw or Decimal('0.00')

        if self.ns_driver_surcharge:
            hire_fee_per_day += self.ns_driver_fee or Decimal('0.00')

        return hire_fee_per_day

    def get_total_hire_fee(self):
        return self.case.invoices.first().total_hire_fee()

    @property
    def formatted_provider(self):
        return self.HireServiceProvider.get_choice(self.provider).label.split(' ')[0].upper()
