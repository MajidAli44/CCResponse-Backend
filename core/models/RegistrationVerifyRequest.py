from django.db import models

from core.models import User


class RegistrationVerifyRequest(models.Model):
    token = models.CharField(max_length=50, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='registration_verify_request')
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
