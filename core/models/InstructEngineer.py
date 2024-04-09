from django.db import models


class InstructEngineer(models.Model):
    email = models.CharField(max_length=255, verbose_name='Email')

    class Meta:
        verbose_name = 'Instruct engineer'
