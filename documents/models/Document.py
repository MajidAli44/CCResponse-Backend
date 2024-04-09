from django.contrib.postgres.fields import ArrayField
from django.db import models

from common.models import BaseAbstractModel


class Document(BaseAbstractModel):

    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='documents', blank=True, null=True)
    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='documents', blank=True, null=True)
    introducer = models.ForeignKey('parties.Introducer', on_delete=models.CASCADE, related_name='documents', blank=True, null=True)
    solicitor = models.ForeignKey('parties.Solicitor', on_delete=models.CASCADE, related_name='documents', blank=True, null=True)

    rel_file_path = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)

    empty_fields = ArrayField(base_field=models.CharField(max_length=64), default=list, blank=True, null=True)

    is_invoice = models.BooleanField(default=False)
    auto_generated_document = models.BooleanField(default=False)
    document_need_sign = models.BooleanField(default=False)
    display_document_in_table = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
