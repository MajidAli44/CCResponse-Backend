from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from chat.models import ChatMessage


class ChatMessageCreateSerializer(serializers.ModelSerializer):

    filename = serializers.CharField(required=False)

    legal_extensions = [
        'jpeg', 'jpg', 'png', 'gif',
        'mp4', 'mpeg', 'ogg', 'webm',
        'quicktime', 'csv', 'pdf'
    ]

    class Meta:
        model = ChatMessage
        fields = ('message_type', 'content', 'filename')

    def validate(self, attrs):

        message_type = attrs.get('message_type', None)
        filename = attrs.get('filename', None)
        if message_type in [ChatMessage.MessageType.image, ChatMessage.MessageType.video, ChatMessage.MessageType.file]:
            if filename is None:
                raise ValidationError({'filename': 'the field must not be empty'})

            if '.' not in filename:
                raise ValidationError({'filename': 'invalid filename format'})

            filename_split = filename.split('.')
            filename_extension = filename_split[len(filename_split) - 1]

            if filename_extension not in self.legal_extensions:
                raise ValidationError({'filename': 'illegal file extension'})

        return super(ChatMessageCreateSerializer, self).validate(attrs)
