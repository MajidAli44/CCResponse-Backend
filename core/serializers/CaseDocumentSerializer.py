from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import CaseDocument


class CaseDocumentSerializer(serializers.ModelSerializer):
    filename = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(read_only=True)
    username = serializers.CharField(max_length=301, read_only=True, source='user.fullname')

    class Meta:
        model = CaseDocument
        fields = ('id', 'user', 'username', 'case', 'filename', 'file', 'type', 'description', 'created_at')

    def validate(self, attrs):
        request = self.context.get('request', None)
        user = request.user if request else None
        if user and user.pk:
            attrs['user'] = user
        else:
            raise ValidationError({'user': "Can't determine user uploaded this file"})

        if case := self.context.get('case', None):
            attrs['case'] = case
        return super().validate(attrs)

    def get_filename(self, obj):
        return obj.file.name.split('/')[-1]
