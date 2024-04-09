from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models

from djchoices import DjangoChoices, ChoiceItem

from core.models import Vehicle, Customer, ExternalParty, ThirdParty, User


class Case(models.Model):
    class Status(DjangoChoices):
        ongoing = ChoiceItem('ongoing', 'Ongoing')
        payment_pack = ChoiceItem('payment_pack', 'Payment Pack')
        settled = ChoiceItem('settled', 'Settled')
        rejected = ChoiceItem('rejected', 'Rejected')

    class Circumstances(DjangoChoices):
        tired = ChoiceItem('tired', 'Tired')
        sleepy = ChoiceItem('sleepy', 'Sleepy')
        rainy = ChoiceItem('rainy', 'Rainy')

    class PaymentStatus(DjangoChoices):
        paid = ChoiceItem('paid', 'Paid')
        unpaid = ChoiceItem('unpaid', 'Unpaid')
        waiting = ChoiceItem('waiting', 'Waiting')

    class Priority(DjangoChoices):
        not_interested = ChoiceItem('not_interested', 'Not Interested')

    customer_vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL,
                                         related_name='customer_vehicle_cases', null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='customer_cases', null=True)
    external_parties = models.ManyToManyField(ExternalParty, through='ExternalPartyService',
                                              related_name='external_party_cases')
    third_party = models.ForeignKey(ThirdParty, on_delete=models.SET_NULL, related_name='third_party_cases', null=True)
    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='worker_cases')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    instruction_date = models.DateField(blank=True, null=True)
    date_retained = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    date_of_accident = models.DateField()
    time_of_accident = models.TimeField(blank=True, null=True)
    location = models.TextField(blank=True)
    status = models.CharField(choices=Status.choices, max_length=30, default=Status.ongoing)
    priority = models.CharField(max_length=50, blank=True, null=True, choices=Priority.choices)
    finished_at = models.DateTimeField(blank=True, null=True)
    hire_details = models.TextField(blank=True)
    hire_validation = models.TextField(blank=True)
    hire_settlement_details = models.TextField(blank=True)
    recovery_details = models.TextField(blank=True)
    recovery_settlement_details = models.TextField(blank=True)
    storage_details = models.TextField(blank=True)
    storage_settlement_details = models.TextField(blank=True)
    clawback_details = models.TextField(blank=True)
    weather = models.TextField(blank=True)
    circumstances = models.CharField(choices=Circumstances.choices, max_length=30, blank=True)
    payment_status = models.CharField(choices=PaymentStatus.choices, max_length=200, blank=True)
    ack_comms = models.BooleanField(default=False)
    communication = models.CharField(blank=True, max_length=200)
    other_info = models.TextField(blank=True)
    should_show_hire_sr = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.customer_vehicle and self.customer_vehicle.owner != Vehicle.Owner.customer:
            raise DjangoValidationError(f"Case(pk={self.pk}) can only have customer_vehicle with owner=customer")
        super().save(*args, **kwargs)

    def __str__(self):
        if self.customer and self.customer_vehicle:
            return f'{self.customer}\'s case ' \
                   f'at the {self.customer_vehicle.vrn} ' \
                   f'on {self.date_of_accident.strftime("%b %d %Y")}'
        return f'Customer case id={self.pk} on {self.date_of_accident.strftime("%b %d %Y")}'
