from rest_framework import serializers

from cases.models import CaseFieldsDefaultPrice


class CaseFieldsDefaultPriceSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(CaseFieldsDefaultPriceSerializer, self).__init__(*args, **kwargs)
        self.fields.pop('id')

    class Meta:
        model = CaseFieldsDefaultPrice
        fields = '__all__'
