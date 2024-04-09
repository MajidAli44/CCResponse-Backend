from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from core.models import Vehicle, ThirdParty, ExternalParty, Address
from .PartyVehicleSerializer import PartyVehicleSerializer
from .ThirdPartyInsurerSerializer import ThirdPartyInsurerSerializer
from .VehicleSerializer import VehicleSerializer


class ThirdPartySerializer(ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=200)
    vehicle = PartyVehicleSerializer(required=False)
    insurer = ThirdPartyInsurerSerializer(required=False)
    address = serializers.CharField(source='address.address')

    class Meta:
        model = ThirdParty
        fields = '__all__'

    def validate(self, attrs):
        name = attrs.get('name', None)
        tp_id = attrs.get('id', None)
        qs = ThirdParty.objects.filter(name=name)
        if tp_id:
            qs = qs.exclude(id=tp_id)
        if name and qs.exists():
            raise ValidationError({'name': 'party with this name already exists.'})
        if isinstance((adress_dict := attrs.get('address', None)), dict):
            attrs['address'] = adress_dict['address']
        if not attrs.get('address', None):
            raise ValidationError({'address': "address shouldn't be null or empty"})

        if tp_vehicle := attrs.get('vehicle', {}):
            try:
                VehicleSerializer(
                    instance=Vehicle.objects.filter(
                        id=tp_vehicle.get('id', None),
                        owner=Vehicle.Owner.third_party
                    ).first(),
                    data={
                        **tp_vehicle,
                        'owner': Vehicle.Owner.third_party
                    }
                ).is_valid(raise_exception=True)
            except ValidationError as e:
                raise ValidationError({'vehicle': e.detail})

        if tp_insurer := attrs.get('insurer', {}):
            try:
                ThirdPartyInsurerSerializer(
                    instance=ExternalParty.objects.filter(
                        id=tp_insurer.get('id', None),
                        role=ExternalParty.Role.insurer,
                        is_third_party=True
                    ).first(),
                    data={
                        **tp_insurer,
                        'role': ExternalParty.Role.insurer,
                        'is_third_party': True
                    }
                ).is_valid(raise_exception=True)
            except ValidationError as e:
                raise ValidationError({'insurer': e.detail})

        return attrs

    @staticmethod
    def __get_third_party_vehicle(third_party_vehicle_data):
        if not third_party_vehicle_data:
            return None

        tp_vehicle_serializer = VehicleSerializer(
            instance=Vehicle.objects.filter(
                id=third_party_vehicle_data.get('id', None),
                owner=Vehicle.Owner.third_party
            ).first(),
            data={
                **third_party_vehicle_data,
                'owner': Vehicle.Owner.third_party
            }
        )
        try:
            tp_vehicle_serializer.is_valid(raise_exception=True)
            vehicle = tp_vehicle_serializer.save()
        except ValidationError as e:
            raise ValidationError({'vehicle': e.detail})
        return vehicle

    @staticmethod
    def __get_third_party_insurer(third_party_insurer_data):
        if not third_party_insurer_data:
            return None

        tp_insurer_serializer = ThirdPartyInsurerSerializer(
            instance=ExternalParty.objects.filter(
                id=third_party_insurer_data.get('id', None),
                role=ExternalParty.Role.insurer,
                is_third_party=True
            ).first(),
            data={
                **third_party_insurer_data,
                'role': ExternalParty.Role.insurer,
                'is_third_party': True
            }
        )
        try:
            tp_insurer_serializer.is_valid(raise_exception=True)
            insurer = tp_insurer_serializer.save()
        except ValidationError as e:
            raise ValidationError({'insurer': e.detail})
        return insurer

    def create(self, validated_data):
        third_party_vehicle = self.__get_third_party_vehicle(validated_data.pop('vehicle', {}))
        third_party_insurer = self.__get_third_party_insurer(validated_data.pop('insurer', {}))
        address = Address.objects.get_or_create(address=validated_data.pop('address'))[0]

        return super().create(
            {
                **validated_data,
                'vehicle': third_party_vehicle,
                'insurer': third_party_insurer,
                'address': address
            }
        )

    def update(self, instance, validated_data):
        third_party_vehicle = self.__get_third_party_vehicle(validated_data.pop('vehicle', {}))
        third_party_insurer = self.__get_third_party_insurer(validated_data.pop('insurer', {}))
        address = Address.objects.get_or_create(address=validated_data.pop('address'))[0]

        return super().update(
            instance,
            {
                **validated_data,
                'vehicle': third_party_vehicle,
                'insurer': third_party_insurer,
                'address': address
            }
        )

