from rest_framework import serializers

from core.models import Expense, Vehicle


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'date', 'description', 'cost', 'vehicle')
        read_only_fields = ('vehicle',)

    def validate(self, attrs):
        request = self.context.get('request', None)
        if request.method == "POST":
            vehicle_id = request and request.query_params.get('vehicle_id', None)
            vehicle = Vehicle.objects.filter(pk=vehicle_id).first()
            if vehicle is None:
                raise serializers.ValidationError({
                    'vehicle_id': "You either didn't specified vehicle_id "
                                  "in query parameters or vehicle doesn't exist"
                })
            attrs['vehicle'] = vehicle
        return attrs
