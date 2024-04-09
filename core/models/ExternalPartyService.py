from django.db import models
from django.utils import timezone

from core.models import ExternalParty, Case


class ExternalPartyService(models.Model):
    external_party = models.ForeignKey(ExternalParty, on_delete=models.SET_NULL, null=True,
                                       related_name='external_party_services')
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True, related_name='related_external_parties')
    joined_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    finish_work_at = models.DateField(blank=True, null=True)
    introducer_fee = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    def __str__(self):
        if self.external_party and self.case:
            return f'{self.external_party} works with {self.case}'
        return f'External party service with id = {self.pk}'

    def save(self, *args, **kwargs):
        if not self.introducer_fee:
            self.introducer_fee = self.external_party.introducer_fee
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['external_party', 'case'], name='unique_service')
        ]
