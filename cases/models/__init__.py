from django.db.models.signals import post_save
from django.dispatch import receiver

from .Accident import Accident
from .Case import Case
from .CaseFieldsDefaultPrice import CaseFieldsDefaultPrice
from .CaseNote import CaseNote
from .ClawbackDetail import ClawbackDetail
from .FollowUp import FollowUp
from .HireDetail import HireDetail
from .HireValidation import HireValidation
from .HireAgreement import HireAgreement
from .PIDetail import PIDetail
from .RecoveryDetail import RecoveryDetail
from .StorageDetail import StorageDetail
from .UserDisplayCaseColumn import UserDisplayCaseColumn
from .CaseFee import CaseFee

__all__ = [
    'Case', 'Accident', 'PIDetail', 'FollowUp', 'RecoveryDetail', 'ClawbackDetail', 'HireDetail', 'CaseNote',
    'UserDisplayCaseColumn', 'CaseFieldsDefaultPrice', 'HireValidation', 'HireAgreement', 'CaseFee'
]


@receiver(post_save, sender=Case)
def generate_auto_docs(**kwargs):
    pass


@receiver(post_save, sender=Case)
def generate_invoices(instance, created, **kwargs):
    if created:
        from invoices.models import Invoice
        case_invoices = []
        for invoice_type in Invoice.InvoiceType.labels:
            case_invoices.append(Invoice(charge_type=invoice_type, case=instance))
        Invoice.objects.bulk_create(case_invoices)
