from django.db import models

from core.models import User


class EmailVerifyRequest(models.Model):
    token = models.CharField(max_length=50, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='email_verify_request')
    created_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']
