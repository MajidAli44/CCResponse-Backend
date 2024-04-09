from django.utils import timezone
from rest_framework import serializers

from core.models import ScheduledToChaseCase


class ScheduledToChaseCaseSerializer(serializers.ModelSerializer):
    is_overdued = serializers.SerializerMethodField()

    class Meta:
        model = ScheduledToChaseCase
        fields = ('id', 'case', 'chase_date', 'is_overdued')

    def get_is_overdued(self, obj):
        return (timezone.now().date() - obj.chase_date).days > 0
