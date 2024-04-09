from rest_framework import serializers

from chat.models import ChatMessage


class ChatMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatMessage
        fields = (
            'id', 'created_at', 'updated_at', 'case', 'author', 'author_name', 'source', 'message_type', 'content',
            'filename', 'twilio_message_sid', 'twilio_message_status'
        )

