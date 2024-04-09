from rest_framework.serializers import ModelSerializer

from core.models import Message
from .AttachmentSerializer import AttachmentSerializer


class MessageSerializer(ModelSerializer):
    attachments = AttachmentSerializer(many=True)

    class Meta:
        model = Message
        fields = ('id', 'subject', 'message', 'attachments', 'received_at', 'is_read', 'sender')
