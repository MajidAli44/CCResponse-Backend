from django.db import models
from ccresponse.storage_backends import PrivateMediaStorage

from core.models import Case, User


class CaseDocument(models.Model):
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='case_documents', storage=PrivateMediaStorage())
    type = models.CharField(max_length=40, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
