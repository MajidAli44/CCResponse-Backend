from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from ccresponse.storage_backends import PrivateMediaStorage
from core.models import Message


class Attachment(models.Model):
    class Type(DjangoChoices):
        image = ChoiceItem()
        video = ChoiceItem()
        audio = ChoiceItem()

    message = models.ForeignKey(Message, on_delete=models.SET_NULL, related_name='attachments', null=True)
    type = models.CharField(choices=Type.choices, max_length=30)
    attachment = models.FileField(upload_to='attachments/', storage=PrivateMediaStorage())

    def __str__(self):
        custom_string = f'{self.type.title()} attachment'
        if self.message:
            return f'{custom_string} of {self.message.sender} in {self.message.chat}'
        return custom_string
