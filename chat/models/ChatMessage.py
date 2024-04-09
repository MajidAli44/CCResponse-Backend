from datetime import datetime, timezone

from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from cases.models import Case
from common.models import BaseAbstractModel
from common.services.StorageService import storageService
from core.models import User


class ChatMessage(BaseAbstractModel):

    class MessageAuthor(DjangoChoices):
        client = ChoiceItem('client', 'Client')
        manager = ChoiceItem('manager', 'Manager')

    class MessageType(DjangoChoices):
        text = ChoiceItem('text', 'Text')
        image = ChoiceItem('image', 'Image')
        video = ChoiceItem('video', 'Video')
        audio = ChoiceItem('audio', 'Audio')
        file = ChoiceItem('file', 'File')

    class MessageSource(DjangoChoices):
        crm = ChoiceItem('crm', 'CRM')
        whats_app = ChoiceItem('whatsapp', 'WhatsApp')

    class TwilioMessageStatus(DjangoChoices):
        queued = ChoiceItem('queued', 'Queued')
        sent = ChoiceItem('sent', 'Sent')
        delivered = ChoiceItem('delivered', 'Delivered')
        received = ChoiceItem('received', 'Received')
        read = ChoiceItem('read', 'Read')

    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True, blank=True, related_name='chat_messages')
    author = models.CharField(choices=MessageAuthor.choices, max_length=7)
    author_name = models.CharField(max_length=512, blank=True, null=True)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    source = models.CharField(choices=MessageSource.choices, max_length=8)
    message_type = models.CharField(choices=MessageType.choices, max_length=5)
    content = models.TextField(blank=True, null=True)

    filename = models.CharField(max_length=512, blank=True, null=True)
    pre_signed_url = models.CharField(max_length=1024, blank=True, null=True)
    pre_signed_url_generated_at = models.DateTimeField(blank=True, null=True)

    twilio_message_sid = models.CharField(max_length=512, blank=True, null=True)
    twilio_message_status = models.CharField(choices=TwilioMessageStatus.choices, max_length=9, blank=True, null=True)

    class Meta:
        indexes = [models.Index(fields=['case']), models.Index(fields=['twilio_message_sid'])]

    def get_content(self):
        """
        Метод позволяющий получить контент текущего сообщения из чата

        Если тип сообщения text - возвращаем поле content

        В противном случае мы проверяем наличие подписанной ссылки
        Если ссылки нет - генерируем и сохраняем, что бы потом возвращать "кэшированную" ссылку

        Если ссылка присутствует - проверяем время её действия
        Если время действия подходит к концу, то перегенерируем её
        """
        if self.message_type not in [self.MessageType.image, self.MessageType.video, self.MessageType.file, self.MessageType.audio]:
            return self.content

        if self.pre_signed_url is None:
            self.__generate_pre_signed_url()

        time_elapsed_from_pre_sign_url = datetime.now(timezone.utc) - self.pre_signed_url_generated_at
        if time_elapsed_from_pre_sign_url.days >= 6:
            self.__generate_pre_signed_url()

        return self.pre_signed_url

    def __generate_pre_signed_url(self):
        """
        Метод генерируеющий pre signed url для файла
        Время жизни ссылки 7 дней
        После генерации обновляется поле со ссылкой и датой генерации
        """
        self.pre_signed_url = storageService.get_s3_presigned_url(self.content, expiration=60 * 60 * 24 * 7)  # 7 days
        self.pre_signed_url_generated_at = datetime.now(timezone.utc)
        self.save()
