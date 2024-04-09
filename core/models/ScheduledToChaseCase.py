from django.db import models

from core.models import Case, User


class ScheduledToChaseCase(models.Model):
    case = models.OneToOneField(Case, on_delete=models.CASCADE, related_name='scheduled_to_chase_case')
    chase_date = models.DateField()
    user_last_scheduled = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
