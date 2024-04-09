from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from common.models import BaseAbstractModel
from documents.models import Document


class DocumentSignature(BaseAbstractModel):
    class Statuses(DjangoChoices):
        created = ChoiceItem('created', 'Created')
        sent = ChoiceItem('sent', 'Sent')
        delivered = ChoiceItem('delivered', 'Delivered')
        signed = ChoiceItem('signed', 'Signed')
        completed = ChoiceItem('completed', 'Completed')
        declined = ChoiceItem('declined', 'Declined')
        voided = ChoiceItem('voided', 'Voided')
        deleted = ChoiceItem('deleted', 'Deleted')

    document = models.OneToOneField(Document, on_delete=models.CASCADE, related_name='document_signature')
    recipient = models.EmailField()
    recipient_name = models.CharField(max_length=127)
    message = models.TextField(blank=True, null=True)
    status = models.CharField(choices=Statuses.choices, max_length=9, default=Statuses.created)
    envelope_id = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Document signature'
        verbose_name_plural = 'Document signatures'
