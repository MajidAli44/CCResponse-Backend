from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class VehicleActionSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if 'end_date' not in attrs:
            raise ValidationError(
                {
                    'end_date': 'You should specify end_date as you have specified any other key, '
                                'i.e start_date or vehicle! end_date should be either a valid date or null in this case'
                }
            )
        if attrs['end_date'] and attrs['end_date'] <= attrs['start_date']:
            raise serializers.ValidationError({'end_date': "End date should be greater than start date"})
        return attrs
