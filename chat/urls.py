from django.urls import path, include

from chat.views import ChatMessagesListCreateAPIView, WhatsAppChatActivateAPIView, WhatsAppChatCallbackAPIView, \
    WhatsAppChatStatusCallbackAPIView

urlpatterns = [
    path('<int:case_id>/', include([
        path('', ChatMessagesListCreateAPIView.as_view()),
        path('whatsapp/activate/', WhatsAppChatActivateAPIView.as_view()),
    ])),
    path('whatsapp/callback/message/', WhatsAppChatCallbackAPIView.as_view()),
    path('whatsapp/callback/status/', WhatsAppChatStatusCallbackAPIView.as_view())
]
