from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import ChatMessage


class WhatsAppChatStatusCallbackAPIView(APIView):

    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        message_sid = request.POST.get('SmsSid')
        message_status = request.POST.get('MessageStatus')

        chat_message = ChatMessage.objects.get(twilio_message_sid=message_sid)
        chat_message.twilio_message_status = message_status
        chat_message.save()

        return Response({'status': 'OK'}, status=status.HTTP_200_OK)
