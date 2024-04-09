from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models

from core.models import Party, ExternalParty
from .Vehicle import Vehicle


class ThirdParty(Party):
    vehicle = models.ForeignKey('Vehicle', on_delete=models.SET_NULL, related_name='vehicle_third_parties', null=True)
    insurer = models.ForeignKey(ExternalParty, on_delete=models.SET_NULL,
                                related_name='insurer_third_parties', null=True)
    policy_number = models.CharField(max_length=200, blank=True)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL,
                                related_name='third_parties', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Third parties'

    def save(self, *args, **kwargs):
        if self.vehicle and self.vehicle.owner != Vehicle.Owner.third_party:
            raise DjangoValidationError(f"ThirdParty(pk={self.pk}) can only have vehicle with owner=third_party")
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Third party {self.name}'
