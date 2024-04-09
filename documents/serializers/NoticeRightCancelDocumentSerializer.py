from datetime import date

from rest_framework import serializers

from cases.models import Case


class NoticeRightCancelDocumentSerializer(serializers.ModelSerializer):

    current_date = serializers.SerializerMethodField()
    client_name = serializers.CharField(source='client.name', allow_null=True)
    client_address = serializers.CharField(source='client.address', allow_null=True)

    class Meta:
        model = Case
        fields = ('current_date', 'client_name', 'client_address')

    def get_current_date(self, _obj):
        return date.today().strftime("%d/%m/%Y")
