from django.db import models

from .User import User


class PasswordResetRequest(models.Model):

    token = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
