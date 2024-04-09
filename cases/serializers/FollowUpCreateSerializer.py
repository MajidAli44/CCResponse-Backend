from rest_framework import serializers

from cases.models import FollowUp


class FollowUpCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUp
        fields = (
            'id', 'case', 'date', 'communication',
            'title', 'user', 'created_at'
        )
