from django.db import models

from common.models import BaseAbstractModel


class AbstractParty(BaseAbstractModel):
    """ Abstract model for system`s parties """
    name = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True, help_text='International format')
    email = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    notes = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True, db_index=True)
    postcode = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=["name", ]),
            models.Index(fields=["email", ]),
            models.Index(fields=["address", ]),
        ]

