from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from core.models import User, Party


class Chat(models.Model):
    class Type(DjangoChoices):
        whats_app = ChoiceItem('whats_app', 'WhatsApp')
        crm = ChoiceItem('crm', 'CRM')
        email = ChoiceItem('email', 'Email')

    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='worker_chats')
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True, related_name='party_chats')
    type = models.CharField(choices=Type.choices, max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['worker', 'party', 'type'], name='unique_chat')
        ]

    def __str__(self):
        if self.party and self.worker:
            return f'{self.worker.fullname} and {self.party} {self.get_type_display()} chat'
        return f'Chat with id = {self.pk}'
