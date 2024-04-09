from rest_framework import serializers

from cases.models import FollowUp


class FollowUpUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUp
        fields = ('id', 'is_resolved')
