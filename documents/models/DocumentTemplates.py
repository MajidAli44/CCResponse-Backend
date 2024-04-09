from django.contrib.postgres.fields import ArrayField
from django.db import models

from common.models import BaseAbstractModel


class DocumentTemplates(BaseAbstractModel):

    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='document_templates')
    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='documents_templates', null=True)

    name = models.CharField(max_length=512, blank=True, null=True)
    template_name = models.CharField(max_length=128, blank=True, null=True)

    empty_fields = ArrayField(base_field=models.CharField(max_length=64), default=list, blank=True, null=True)

    document_need_sign = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Document template'
        verbose_name_plural = 'Documents templates'
