from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import User, EmailVerifyRequest, RegistrationVerifyRequest


@receiver(post_save, sender=User)
def user_initial(instance, created, **kwargs):
    if created:
        EmailVerifyRequest.objects.create(user=instance)
        RegistrationVerifyRequest.objects.create(user=instance)
