from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models


class VehicleAction(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def clean(self):
        if self.end_date <= self.start_date:
            raise DjangoValidationError({'end_date': 'End date should be greater that start date'})
