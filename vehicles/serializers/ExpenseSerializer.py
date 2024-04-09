from rest_framework import serializers

from vehicles.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'cost', 'hire_vehicle', 'description', 'expense_date')
        extra_kwargs = {
            'hire_vehicle': {'required': False, 'read_only': True}
        }
