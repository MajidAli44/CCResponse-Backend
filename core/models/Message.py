from django.db import models
from django.utils import timezone

from core.models import Chat


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, related_name='chat_messages', null=True)
    is_worker_sender = models.BooleanField(default=True)
    subject = models.TextField(blank=True)
    message = models.TextField(blank=True)
    received_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender} sent a message in {self.chat}: {self.message}'

    @property
    def sender(self):
        sender = None
        if self.chat:
            worker = self.chat.worker.fullname if self.chat.worker else None
            party = self.chat.party.name if self.chat.party else None
            sender = worker if self.is_worker_sender else party
        return sender or 'Unknown'
