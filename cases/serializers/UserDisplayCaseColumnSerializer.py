from rest_framework import serializers

from cases.models import UserDisplayCaseColumn


class UserDisplayCaseColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDisplayCaseColumn
        fields = (
            'id', 'columns', 'user'
        )
        extra_kwargs = {
            'user': {'read_only': True}
        }
