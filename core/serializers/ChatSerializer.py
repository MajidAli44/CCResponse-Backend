from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Chat
from .MessageSerializer import MessageSerializer


class ChatSerializer(ModelSerializer):
    worker = serializers.CharField(source='worker.fullname')
    party = serializers.CharField(source='party.name')
    chat_messages = MessageSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'worker', 'party', 'type', 'chat_messages')
