from decimal import Decimal as D

from django.db import models
from django.db.models.signals import post_save
from djchoices import DjangoChoices, ChoiceItem

from core.models import Case


# pylint: disable=E1101
class Invoice(models.Model):
    class InvoiceType(DjangoChoices):
        hire = ChoiceItem('hire', 'Hire')
        storage_recovery = ChoiceItem('storage_recovery', 'Storage/Recovery')

    class SettlementStatus(DjangoChoices):
        unsettled = ChoiceItem('unsettled', 'Unsettled')
        settled = ChoiceItem('settled', 'Settled')

    case = models.ForeignKey(Case, on_delete=models.SET_NULL, related_name='invoices', null=True)
    vehicle_hire = models.OneToOneField(
        'VehicleHire', on_delete=models.SET_NULL, related_name='invoice', null=True, blank=True
    )
    vehicle_storage = models.OneToOneField(
        'VehicleStorage', on_delete=models.SET_NULL, related_name='invoice', null=True, blank=True
    )
    vehicle_recovery = models.OneToOneField(
        'VehicleRecovery', on_delete=models.SET_NULL, related_name='invoice', null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    invoice_number = models.CharField(max_length=50)
    settlement_status = models.CharField(
        max_length=100, blank=True, choices=SettlementStatus, default=SettlementStatus.unsettled
    )
    invoice_type = models.CharField(max_length=100, choices=InvoiceType.choices)
    invoice_date = models.DateField()
    date_paid = models.DateField(blank=True, null=True)
    total_net = models.DecimalField(decimal_places=2, max_digits=15, null=True, blank=True)
    total_vat = models.DecimalField(decimal_places=2, max_digits=15, null=True, blank=True)
    settled_amount_net = models.DecimalField(decimal_places=2, max_digits=15, null=True, blank=True)
    settled_amount_vat = models.DecimalField(decimal_places=2, max_digits=15, null=True, blank=True)
    settled_amount_total = models.DecimalField(decimal_places=2, max_digits=15, null=True, blank=True)

    def __str__(self):
        return f'Invoice date: {self.invoice_date}, type: {self.invoice_type}'

    def update_totals(self):
        if not self.total_net and self.invoice_type == self.InvoiceType.hire:
            if self.vehicle_hire and self.vehicle_hire.start_date and self.vehicle_hire.end_date:
                self.total_net = (
                                         self.vehicle_hire.daily_hire_rate or 0
                                 ) * (
                                         (self.vehicle_hire.end_date - self.vehicle_hire.start_date).days + 1
                                 )
            else:
                self.total_net = 0
        if not self.total_net and self.invoice_type == self.InvoiceType.storage_recovery:
            if self.vehicle_storage and self.vehicle_storage.end_date and self.vehicle_storage.start_date:
                self.total_net = (
                        (
                                self.vehicle_storage.daily_storage_rate or 0
                        ) * (
                                (self.vehicle_storage.end_date - self.vehicle_storage.start_date).days + 1
                        )
                )
            else:
                self.total_net = 0

            if self.vehicle_recovery:
                self.total_net = self.total_net + (self.vehicle_recovery.total_price or 0)

        self.total_net = self.total_net or None

        self.total_vat = (
                                 (self.total_net or 0) * D(0.2)
                         ) or None

    def save(self, *args, **kwargs):
        self.update_totals()
        super().save(*args, **kwargs)

    @staticmethod
    def post_save(instance, created, *args, **kwargs):
        case = instance.case
        if created:
            if case and case.status == Case.Status.ongoing:
                case.status = Case.Status.payment_pack
                case.save()
        else:
            if (
                    case and
                    case.invoices.count() == case.invoices.filter(
                settlement_status=Invoice.SettlementStatus.settled
            ).count()
            ):
                case.status = Case.Status.settled
                case.save()


post_save.connect(Invoice.post_save, sender=Invoice, dispatch_uid='invoice_post_save')
