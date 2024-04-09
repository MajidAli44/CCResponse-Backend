import phonenumbers
from djchoices import DjangoChoices, ChoiceItem
from django.db import models

from cases.models import Case
from common.models import BaseAbstractModel


class Chat(BaseAbstractModel):

    class WhatsAppChatStatus(DjangoChoices):
        inactive = ChoiceItem('inactive', 'Inactive')
        pending = ChoiceItem('pending', 'Pending')
        active = ChoiceItem('active', 'Active')

    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='chat')

    whats_app_chat_status = models.CharField(choices=WhatsAppChatStatus.choices, max_length=8, default=WhatsAppChatStatus.inactive)
    whats_app_last_client_message_time = models.DateTimeField(blank=True, null=True)
    whats_app_last_message_time = models.DateTimeField(blank=True, null=True)

    @property
    def phone_number(self):
        client_number = self.case.client_number
        print("client number", client_number)
        if client_number is not None:
            phone = phonenumbers.parse(client_number, region='GB')
            return phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)
        return None

    @staticmethod
    def filter_or_create(case: Case):
        chats = Chat.objects.filter(case=case)
        if len(chats) == 0:
            return Chat.objects.create(case=case, whats_app_chat_status=Chat.WhatsAppChatStatus.inactive)
        return chats[0]
