from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from core.models import Customer, Address


class CustomerSerializer(ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=200)
    address = serializers.CharField(source='address.address')

    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone_number', 'email', 'date_of_birth', 'address',
                  'license_number', 'ni_number', 'notes')

    def validate(self, attrs):
        name = attrs.get('name', None)
        tp_id = attrs.get('id', None)
        qs = Customer.objects.filter(name=name)
        if tp_id:
            qs = qs.exclude(id=tp_id)
        if name and qs.exists():
            raise ValidationError({'name': 'customer with this name already exists.'})
        if isinstance((adress_dict := attrs.get('address', None)), dict):
            attrs['address'] = adress_dict['address']
        if not attrs.get('address', None):
            raise ValidationError({'address': "address shouldn't be null or empty"})
        return attrs

    def create(self, validated_data):
        address = validated_data.pop('address')
        return super().create(
            {
                **validated_data,
                'address': Address.objects.get_or_create(address=address)[0]
            }
        )

    def update(self, instance, validated_data):
        address = validated_data.pop('address')
        return super().update(
            instance,
            {
                **validated_data,
                'address': Address.objects.get_or_create(address=address)[0]
            }
        )
