from rest_framework import serializers

from notification.models import Notification


class UnreadedNotificationSerializer(serializers.ModelSerializer):

    case_id = serializers.IntegerField(source='case.id')
    chat_message = serializers.CharField(source='chat_message.content')
    client_name = serializers.CharField(source='case.client.name')

    class Meta:
        model = Notification
        fields = ('id', 'created_at', 'updated_at', 'case_id', 'client_name', 'is_read', 'chat_message')
