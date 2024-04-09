from django.db import models

from common.models import BaseAbstractModel


class AbstractVehicle(BaseAbstractModel):
    vrn = models.CharField(max_length=127, blank=True, null=True, db_index=True)
    make_model = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    mot_expiry = models.DateField(blank=True, null=True, db_index=True)
    tax_expiry = models.DateField(blank=True, null=True, db_index=True)

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=["vrn", ]),
        ]

    @property
    def make(self):
        if self.make_model:
            return self.make_model.split('/')[0]

    @property
    def model(self):
        if self.make_model:
            try:
                return self.make_model.split('/')[1]
            except IndexError:
                return self.make_model.split()[-1]
