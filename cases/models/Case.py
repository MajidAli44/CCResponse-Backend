from datetime import date
from decimal import Decimal

from django.contrib.postgres.fields import ArrayField
from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from common.models import BaseAbstractModel
from core.models import User
from parties.models import Client, ThirdParty, Solicitor, Introducer, Provider


class Case(BaseAbstractModel):
    """Model for case"""

    class CaseStatuses(DjangoChoices):
        lead = ChoiceItem('lead', 'Lead')
        ongoing = ChoiceItem('ongoing', 'Ongoing')
        payment_pack = ChoiceItem('payment_pack', 'Payment Pack')
        settled = ChoiceItem('settled', 'Settled')
        closed = ChoiceItem('closed', 'Closed')

    class CaseStatusDescription(DjangoChoices):
        lead_new_lead = ChoiceItem('lead_new_lead', 'New Lead')
        lead_no_answer = ChoiceItem('lead_no_answer', 'No Answer')
        lead_awaiting_further_info = ChoiceItem('lead_awaiting_further_info', 'Await more Info')
        lead_hk_to_provider = ChoiceItem('lead_hk_to_provider', 'HK to Provider')

        ongoing_accepted = ChoiceItem('ongoing_accepted', 'Accepted')
        ongoing_in_hire = ChoiceItem('ongoing_in_hire', 'In hire')

        payment_pack_pp_issued = ChoiceItem('payment_pack_pp_issued', 'PP Submitted')
        payment_pack_settlement_agreed = ChoiceItem('payment_pack_settlement_agreed', 'Settlement Agreed')
        payment_pack_passed_to_ra = ChoiceItem('payment_pack_passed_to_ra', 'Litigated')

        settled_closed_no_contact = ChoiceItem('settled_closed_no_contact', 'Closed - Failed Contact')
        settled_closed_poor_prospects = ChoiceItem('settled_closed_poor_prospects', 'Closed - Poor Prospects')
        settled_closed_client_dwtp = ChoiceItem('settled_closed_client_dwtp', 'Client DWTP')
        settled_closed_abandoned_recovery = ChoiceItem('settled_closed_abandoned_recovery', 'Abandoned Recovery')
        settled_closed_file_settled = ChoiceItem('settled_closed_file_settled', 'File Settled')
        awaiting_bid = ChoiceItem('awaiting_bid', 'Awaiting Bid')
        pending_hire = ChoiceItem('pending_hire', 'Pending Hire')

    class PaymentStatuses(DjangoChoices):
        paid = ChoiceItem('paid', 'Paid')
        unpaid = ChoiceItem('unpaid', 'Unpaid')
        waiting = ChoiceItem('waiting', 'Waiting')

    class CaseSource(DjangoChoices):
        google = ChoiceItem('google', 'Google')

    class RecoveryAgent(DjangoChoices):
        cc_response = ChoiceItem('cc_response', 'CC Response')
        canfords = ChoiceItem('canfords', 'Canfords')
        barings = ChoiceItem('barings', 'Barings')
        dgm = ChoiceItem('dgm', 'DGM')

    class Services(DjangoChoices):
        cd = ChoiceItem('cd', 'Claim Details')
        hd = ChoiceItem('hd', 'Hire Details')
        sr = ChoiceItem('sr', 'Storage Recovery')
        pi = ChoiceItem('pi', 'Personal Injury')
        vd = ChoiceItem('vd', 'Vehicle Damage')
        sv = ChoiceItem('sv', 'Salvage')

    client = models.OneToOneField(
        Client, on_delete=models.SET_NULL, related_name='cases',
        blank=True, null=True
    )
    case_creator = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='case_creator'
    )
    file_handler = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='file_handler'
    )
    accident = models.OneToOneField(
        'Accident', on_delete=models.SET_NULL, blank=True, null=True
    )
    third_party = models.OneToOneField(
        ThirdParty, on_delete=models.SET_NULL, blank=True, null=True
    )
    solicitor = models.ForeignKey(
        Solicitor, on_delete=models.SET_NULL, blank=True, null=True
    )
    solicitor_ref = models.CharField(max_length=255, blank=True, null=True)
    introducer = models.ForeignKey(
        Introducer, on_delete=models.SET_NULL, blank=True, null=True
    )
    introducer_fee = models.FloatField(blank=True, null=True)
    provider = models.ForeignKey(
        Provider, on_delete=models.SET_NULL, blank=True, null=True
    )
    clawback_detail = models.OneToOneField(
        'ClawbackDetail', on_delete=models.SET_NULL, blank=True, null=True
    )
    storage_detail = models.OneToOneField(
        'StorageDetail', on_delete=models.SET_NULL, blank=True, null=True
    )
    hire_detail = models.OneToOneField(
        'HireDetail', on_delete=models.SET_NULL, blank=True, null=True
    )
    hire_validation = models.OneToOneField(
        'HireValidation', on_delete=models.SET_NULL, blank=True, null=True
    )
    hire_agreement = models.OneToOneField(
        'HireAgreement', on_delete=models.SET_NULL, blank=True, null=True
    )
    recovery_detail = models.OneToOneField(
        'RecoveryDetail', on_delete=models.SET_NULL, blank=True, null=True
    )
    pi_detail = models.OneToOneField(
        'PIDetail', on_delete=models.SET_NULL, blank=True, null=True
    )
    payment_status = models.CharField(
        choices=PaymentStatuses.choices, max_length=50, blank=True, null=True
    )
    case_fee = models.OneToOneField(
        'CaseFee', on_delete=models.SET_NULL, blank=True, null=True
    )
    repair_invoice = models.OneToOneField(
        'invoices.RepairInvoice', on_delete=models.SET_NULL, blank=True, null=True
    )

    status = models.CharField(default=CaseStatuses.lead, choices=CaseStatuses.choices, max_length=50)
    status_description = models.CharField(default=CaseStatusDescription.lead_awaiting_further_info,
                                          choices=CaseStatusDescription.choices, max_length=50, blank=True, null=True)
    case_source = models.CharField(choices=CaseSource.choices, max_length=32, blank=True, null=True)
    recovery_agent = models.CharField(choices=RecoveryAgent.choices, max_length=32, blank=True, null=True)

    instruction_date = models.DateField(default=date.today, blank=True, null=True)
    retained_date = models.DateField(blank=True, null=True)
    services = ArrayField(
        models.CharField(choices=Services.choices, max_length=20),
        default=["cd"],
        size=6,
    )

    class Meta:
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'
        ordering = ['-created_at']

    @property
    def cc_ref(self):
        return f'CC/{self.pk}'

    @property
    def client_number(self):
        if self.client is None:
            return None
        return self.client.phone_number

    @property
    def service_providers(self):
        providers = []
        if self.hire_detail.provider is not None:
            providers.append(self.hire_detail.formatted_provider)
        if self.storage_detail.provider is not None:
            providers.append(self.storage_detail.formatted_provider)
        if self.pi_detail.provider is not None:
            providers.append(self.pi_detail.formatted_provider)
        return '/'.join(providers)

    @property
    def case_value(self):
        invoice = self.invoices.first()
        total = invoice.total_hire_fee() + invoice.total_storage_fee()
        return total

    @staticmethod
    def get_available_status_descriptions():
        return [
            {
                'status': Case.CaseStatuses.lead,
                'accepted_descriptions': [
                    Case.CaseStatusDescription.lead_new_lead,
                    Case.CaseStatusDescription.lead_no_answer,
                    Case.CaseStatusDescription.lead_awaiting_further_info,
                    Case.CaseStatusDescription.lead_hk_to_provider
                ],
                'default': Case.CaseStatusDescription.lead_new_lead
            },
            {
                'status': Case.CaseStatuses.ongoing,
                'accepted_descriptions': [
                    Case.CaseStatusDescription.ongoing_accepted,
                    Case.CaseStatusDescription.ongoing_in_hire
                ],
                'default': Case.CaseStatusDescription.ongoing_accepted
            },
            {
                'status': Case.CaseStatuses.payment_pack,
                'accepted_descriptions': [
                    Case.CaseStatusDescription.payment_pack_pp_issued,
                    Case.CaseStatusDescription.payment_pack_settlement_agreed,
                    Case.CaseStatusDescription.payment_pack_passed_to_ra
                ],
                'default': Case.CaseStatusDescription.payment_pack_pp_issued
            },
            {
                'status': Case.CaseStatuses.settled,
                'accepted_descriptions': [
                    Case.CaseStatusDescription.settled_closed_no_contact,
                    Case.CaseStatusDescription.settled_closed_poor_prospects,
                    Case.CaseStatusDescription.settled_closed_client_dwtp,
                    Case.CaseStatusDescription.settled_closed_abandoned_recovery,
                    Case.CaseStatusDescription.settled_closed_file_settled
                ],
                'default': Case.CaseStatusDescription.settled_closed_client_dwtp
            },
            {
                'status': Case.CaseStatuses.closed,
                'accepted_descriptions': [
                    Case.CaseStatusDescription.settled_closed_no_contact,
                    Case.CaseStatusDescription.settled_closed_poor_prospects,
                    Case.CaseStatusDescription.settled_closed_client_dwtp,
                    Case.CaseStatusDescription.settled_closed_abandoned_recovery,
                    Case.CaseStatusDescription.settled_closed_file_settled
                ],
                'default': Case.CaseStatusDescription.settled_closed_no_contact
            }
        ]
