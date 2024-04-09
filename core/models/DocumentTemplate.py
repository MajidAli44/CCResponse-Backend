from django.db import models

from ccresponse.storage_backends import PrivateMediaStorage
from core.models import User


class DocumentTemplate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='document_templates', null=True)
    name = models.CharField(max_length=250, unique=True)
    template_file = models.FileField(upload_to='document_templates/', storage=PrivateMediaStorage())

    def __str__(self):
        return self.name
