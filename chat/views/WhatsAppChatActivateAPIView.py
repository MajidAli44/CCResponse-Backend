from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cases.models import Case
from ccresponse import settings
from chat.models import ChatMessage
from chat.models.Chat import Chat
from chat.serializers import ChatMessageSerializer
from chat.services.WhatsAppService import WhatsAppService


class WhatsAppChatActivateAPIView(APIView):

    whats_app_service = WhatsAppService(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_ACCOUNT_AUTH_TOKEN)
    chat_message_response = openapi.Response(description='OK', schema=ChatMessageSerializer)

    @swagger_auto_schema(
        operation_description='Метод предназначенный для активации чата',
        operation_summary='Активация чата отправкой шаблона',
        responses={
            200: chat_message_response,
            404: 'Client phone number not found',
            400: 'Validation errors',
        }
    )
    def post(self, request, *args, **kwargs):
        case_id = self.kwargs.get('case_id')
        case = get_object_or_404(Case, id=case_id)
        chat = Chat.filter_or_create(case=case)

        if chat.phone_number is None:
            return Response(data={'message': 'the client phone number was not found'}, status=status.HTTP_404_NOT_FOUND)

        if chat.whats_app_chat_status != Chat.WhatsAppChatStatus.inactive:
            return Response(data={'message': 'the chat is already in an active or pending state'})

        message = self.whats_app_service.send_template_message(
            phone_number=chat.phone_number, template_name='intro_message',
            client_name=chat.case.client.name, manager_name=request.user.fullname
        )
        print("Message is---",message)
        # Сохраняем время отправки последнего сообщения
        chat.whats_app_last_message_time = message.date_created
        chat.whats_app_chat_status = Chat.WhatsAppChatStatus.pending
        chat.save()

        chat_message = ChatMessage.objects.create(
            case=chat.case, author=ChatMessage.MessageAuthor.manager, author_name=request.user.fullname,
            source=ChatMessage.MessageSource.crm, message_type=ChatMessage.MessageType.text, content=message.body,
            twilio_message_sid=message.sid, twilio_message_status=message.status, author_user=request.user,
        )
        print("WhatsappchatActivate API", chat_message)
        return Response(ChatMessageSerializer(chat_message).data, status=status.HTTP_200_OK)
