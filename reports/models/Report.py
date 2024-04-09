from django.db import models


UNIT_CHOICES = (
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
)


class Report(models.Model):
    title = models.CharField(max_length=100)
    email_addresses = models.TextField(default="")
    filters = models.JSONField()
    time_frequency = models.PositiveIntegerField()
    time_unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    last_run_at = models.DateTimeField(auto_now=True, auto_created=True)
    has_run = models.BooleanField(default=False)

    def get_email_list(self):
        return self.email_addresses.split(',')

    def set_email_list(self, email_list):
        self.email_addresses = ','.join(email_list)

    email_list = property(get_email_list, set_email_list)

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
    
    def __str__(self):
        return f'{self.title} - {self.time_frequency} {self.time_unit}'
