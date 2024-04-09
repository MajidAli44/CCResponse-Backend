from django.db import models

from cases.models import Case
from chat.models import ChatMessage
from common.models import BaseAbstractModel
from core.models import User


class Notification(BaseAbstractModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification')
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='notification')
    chat_message = models.ForeignKey(ChatMessage, on_delete=models.CASCADE, related_name='notification')

    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
