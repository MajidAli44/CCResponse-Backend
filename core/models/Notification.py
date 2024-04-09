from django.db import models

from core.models import User


class Notification(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.worker.fullname} on {self.created_at.strftime("%b %d %Y %H:%M:%S")}'
