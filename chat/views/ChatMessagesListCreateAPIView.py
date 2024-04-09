from base64 import b64decode
from datetime import timedelta, datetime, timezone
from io import BytesIO

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.pagination import SmallLimitOffsetPagination
from cases.models import Case
from ccresponse import settings
from chat.models import ChatMessage
from chat.models.Chat import Chat
from chat.serializers import ChatMessageSerializer, ChatMessageCreateSerializer
from chat.services.WhatsAppService import WhatsAppService
from common.services.StorageService import storageService
from django.core.serializers import serialize
import json


class ChatMessagesListCreateAPIView(ListCreateAPIView):
    pagination_class = SmallLimitOffsetPagination
    permission_classes = (IsAuthenticated,)

    whats_app_service = WhatsAppService(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_ACCOUNT_AUTH_TOKEN)

    image_mimetypes = {
        'jpeg': 'image/jpeg', 'jpg': 'image/jpg', 'gif': 'image/gif', 'png': 'image/png',
        'JPEG': 'image/jpeg', 'JPG': 'image/jpg', 'GIF': 'image/gif', 'PNG': 'image/png',
    }
    audio_mimetypes = {
        'mp4': 'audio/mp4', 'mpeg': 'audio/mpeg', 'ogg': 'audio/ogg', 'webm': 'audio/webm',
        'MP4': 'audio/mp4', 'MPEG': 'audio/mpeg', 'OGG': 'audio/ogg', 'WEBM': 'audio/webm',
    }
    video_mimetypes = {
        'mpeg': 'video/mpeg', 'mp4': 'video/mp4', 'quicktime': 'video/quicktime', 'webm': 'video/webm',
        'MPEG': 'video/mpeg', 'MP4': 'video/mp4', 'QUICKTIME': 'video/quicktime', 'WEBM': 'video/webm',
    }
    files_mimetypes = {
        'csv': 'text/csv', 'pdf': 'application/pdf',
        'CSV': 'text/csv', 'PDF': 'application/pdf',
    }

    chat_message_response = openapi.Response(description='OK', schema=ChatMessageSerializer)

    def get_queryset(self):
        query_set = ChatMessage.objects.filter(case=self.kwargs.get('case_id')).order_by('-created_at')
        return query_set

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ChatMessageSerializer
        return ChatMessageCreateSerializer

    @swagger_auto_schema(
        operation_summary='Получить сообщения из чата',
        operation_description='Метод позволяющий получить сообщения из чата связанного с конкретным кейсом',
    )
    def get(self, request, *args, **kwargs):
        default_response = super().get(request, *args, **kwargs)
        response_data = default_response.data
        print("Chat status is-------")
        # Находим нужный чат
        case = get_object_or_404(Case, pk=self.kwargs.get('case_id'))
        chat = Chat.filter_or_create(case=case)

        if chat.whats_app_last_client_message_time is not None:
            chat_expiry_time = chat.whats_app_last_client_message_time + timedelta(days=1)
            latest = chat_expiry_time - datetime.now(timezone.utc)
            if latest.total_seconds() < 0:
                print("less than 0")
                chat.whats_app_chat_status = Chat.WhatsAppChatStatus.inactive
                chat.save()

        # Добавляем параметры доступности чата
        response_data['chat_status'] = chat.whats_app_chat_status
        response_data['chat_expiry_datetime'] = None if chat.whats_app_last_client_message_time is None else chat_expiry_time
        # Исправляем значение контента
        messages = response_data.get('results')
        for current_message in messages:
            chat_message = get_object_or_404(ChatMessage, pk=current_message.get('id'))
            current_message['content'] = chat_message.get_content()

        return default_response

    @swagger_auto_schema(
        operation_description='Метод предназначенный для отправки сообщений в чат конкретного кейса',
        operation_summary='Отправка сообщения в чат',
        responses={
            200: chat_message_response,
            404: 'Case not found',
            400: 'Validation errors',
        }
    )
    def post(self, request, *args, **kwargs):
        print("requested data----",request.data)
        serializer = ChatMessageCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        message_type = validated_data.get('message_type')
        content = validated_data.get('content')
        filename = validated_data.get('filename')
        case = get_object_or_404(Case, pk=self.kwargs.get('case_id'))
        chat = Chat.filter_or_create(case=case)
        print("chat is---")
        print("before phone numner---")
        print("phone numner---",chat.phone_number)
        print("after phone numner---")
        if chat.whats_app_chat_status != Chat.WhatsAppChatStatus.active:
            return Response({'message': 'chat is not active'}, status=status.HTTP_403_FORBIDDEN)

        if chat.phone_number is None:
            return Response(data={'message': 'the client phone number was not found or not valid'}, status=status.HTTP_404_NOT_FOUND)

        if message_type in [ChatMessage.MessageType.image, ChatMessage.MessageType.video, ChatMessage.MessageType.file]:
            # Save to S3 and put rel file path into content field
            file_extension = filename.split('.')
            file_extension = str(file_extension[len(file_extension) - 1]).lower()
            print("enter into filetype")
            mimetype = None
            if message_type == ChatMessage.MessageType.image and file_extension in self.image_mimetypes:
                mimetype = self.image_mimetypes[file_extension]
            elif message_type == ChatMessage.MessageType.video and file_extension in self.video_mimetypes:
                mimetype = self.video_mimetypes[file_extension]
            elif message_type == ChatMessage.MessageType.audio and file_extension in self.audio_mimetypes:
                mimetype = self.audio_mimetypes[file_extension]
            elif message_type == ChatMessage.MessageType.file and file_extension in self.files_mimetypes:
                mimetype = self.files_mimetypes[file_extension]

            file = BytesIO(b64decode(content))
            content = storageService.put_into_s3_from_stream(file_stream=file, folder='chat/files', file_name=filename, mimetype=mimetype)
        
        chat_message = ChatMessage.objects.create(
            case=case,
            author=ChatMessage.MessageAuthor.manager,
            author_name=request.user.fullname,
            author_user=request.user,
            source=ChatMessage.MessageSource.crm,
            message_type=message_type,
            content=content,
            filename=filename
        )
        print("chatmessage list ",chat_message)
        message_content = chat_message.get_content()
        if message_type == ChatMessage.MessageType.text:
            message = self.whats_app_service.send_text_message(phone_number=chat.phone_number, content=message_content)
        else:
            message = self.whats_app_service.send_file_message(phone_number=chat.phone_number, content=message_content)

        chat_message.twilio_message_sid = message.sid
        chat_message.twilio_message_status = message.status
        chat_message.save()

        return Response(ChatMessageSerializer(chat_message).data, status=status.HTTP_201_CREATED)
