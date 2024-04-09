from rest_framework import serializers

from cases.models import Case


class LetterHeadDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = ()
