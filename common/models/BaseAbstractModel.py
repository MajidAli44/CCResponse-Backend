from django.db import models


class BaseAbstractModel(models.Model):
    """ Base model with timestamps """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.__class__.__name__}: {self.id}'
