from datetime import datetime, timezone
from io import BytesIO

import phonenumbers
import requests
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from cases.models import Case
from chat.models import ChatMessage
from chat.models.Chat import Chat
from common.helpers.CommonHelper import random_string
from common.services.StorageService import storageService
from core.models import User
from documents.models import Document
from notification.models import Notification
from parties.models import Client


class WhatsAppChatCallbackAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        message_sid = request.POST.get('SmsSid')
        message_status = request.POST.get('SmsStatus')
        body = request.POST.get('Body')
        from_ = request.POST.get('From')
        num_media = int(request.POST.get('NumMedia'))

        number = phonenumbers.parse(from_.replace('whatsapp:', ''), region='GB')
        national_phone_number = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL)
        national_without_spaces_phone_number = national_phone_number.replace(' ', '')
        e164_phone_number = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)

        clients = Client.objects.filter(
            Q(phone_number=national_phone_number) |
            Q(phone_number=e164_phone_number) |
            Q(phone_number=national_without_spaces_phone_number)
        ).order_by('-updated_at')
        if len(clients) == 0:
            return Response({'message': f'client with phone number {number} not found'},
                            status=status.HTTP_404_NOT_FOUND)

        current_client = clients.first()
        cases = Case.objects.filter(client=current_client).only('pk')
        active_or_pending_chats = Chat.objects.filter(
            case__in=cases,
            whats_app_chat_status__in=[Chat.WhatsAppChatStatus.active, Chat.WhatsAppChatStatus.pending]
        )

        last_inactive_status = Chat.objects.filter(
            case__in=cases, whats_app_chat_status=Chat.WhatsAppChatStatus.inactive)\
            .order_by('-whats_app_last_message_time')

        chats = []
        if len(active_or_pending_chats) > 0:
            for selected_chat in active_or_pending_chats:
                chats.append(selected_chat)
        elif len(active_or_pending_chats) == 0 and len(last_inactive_status) > 0:
            chats.append(last_inactive_status.first())

        for chat in chats:
            chat.whats_app_chat_status = Chat.WhatsAppChatStatus.active
            chat.whats_app_last_client_message_time = datetime.now(timezone.utc)
            chat.whats_app_last_message_time = datetime.now(timezone.utc)
            chat.save()

            managers = User.objects.all()

            if num_media == 0:
                print("chat message created---")
                chat_message = ChatMessage.objects.create(
                    case=chat.case, author=ChatMessage.MessageAuthor.client,
                    source=ChatMessage.MessageSource.whats_app,
                    message_type=ChatMessage.MessageType.text, content=body, twilio_message_sid=message_sid,
                    twilio_message_status=message_status
                )
            else:
                media_url = request.POST.get('MediaUrl0')
                media_content_type = request.POST.get('MediaContentType0')

                content_type = media_content_type.split('/')[0]
                file_extension = media_content_type.split('/')[1]

                media_bytes = BytesIO()
                with requests.get(media_url, stream=True) as r:
                    r.raise_for_status()
                    media_bytes.write(r.content)

                media_bytes.seek(0)

                filename = f'{random_string(32)}.{file_extension}'
                rel_file_path = storageService.put_into_s3_from_stream(media_bytes, 'chat/files', filename)

                Document.objects.create(
                    case=chat.case, user=None, introducer=None, solicitor=None,
                    rel_file_path=rel_file_path, name=filename, display_document_in_table=True
                )

                chat_message = ChatMessage.objects.create(
                    case=chat.case, author=ChatMessage.MessageAuthor.client,
                    source=ChatMessage.MessageSource.whats_app,
                    message_type=ChatMessage.MessageType.image if content_type == 'image' else
                    ChatMessage.MessageType.video if content_type == 'video' else
                    ChatMessage.MessageType.audio if content_type == 'audio' else
                    ChatMessage.MessageType.file,
                    content=rel_file_path, twilio_message_sid=message_sid,
                    twilio_message_status=message_status
                )
                print("Chat message for file created--",chat_message)
            for current_manager in managers:
                Notification.objects.create(
                    user=current_manager,
                    case=chat.case,
                    chat_message=chat_message
                )

        return Response()
