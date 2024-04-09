from rest_framework import serializers

from cases.models import Accident


class AccidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accident
        fields = (
            'accident_date', 'approx_time', 'location', 'circumstances',
            'weather', 'other_info'
        )
