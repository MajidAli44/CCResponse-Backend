from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from core.models import Vehicle, ExternalPartyService, Case, ThirdParty, Customer, ExternalParty, Injury
from .CustomerSerializer import CustomerSerializer
from .ThirdPartySerializer import ThirdPartySerializer
from .PartyVehicleSerializer import PartyVehicleSerializer
from .ExternalPartyServiceSerializer import ExternalPartyServiceSerializer
from .InjuryCaseSerializer import InjuryCaseSerializer
from .VehicleSerializer import VehicleSerializer


class CaseSerializer(ModelSerializer):
    customer = CustomerSerializer()
    third_party = ThirdPartySerializer()
    customer_vehicle = PartyVehicleSerializer(required=False)
    related_external_parties = ExternalPartyServiceSerializer(many=True, required=False)
    injuries = InjuryCaseSerializer(many=True, required=False)
    follow_up_date = serializers.DateField(source='scheduled_to_chase_case.chase_date', required=False, read_only=True)
    has_bookings = serializers.SerializerMethodField()

    class Meta:
        model = Case
        fields = ('id', 'instruction_date', 'date_of_accident', 'time_of_accident', 'location',
                  'circumstances', 'other_info', 'weather', 'status', 'instruction_date',
                  'date_retained', 'payment_status', 'follow_up_date', 'ack_comms', 'customer',
                  'third_party', 'communication', 'related_external_parties', 'injuries', 'customer_vehicle',
                  'has_bookings', 'should_show_hire_sr',
                  )
        depth = 1

    def get_has_bookings(self, obj):
        return obj.hires.all().exists()

    def validate(self, attrs):
        customer = attrs.get('customer', {})
        third_party = attrs.get('third_party', {})
        third_party_insurer = third_party.get('insurer', {})
        external_parties = attrs.get('related_external_parties', {})
        names = [customer.get('name'), third_party.get('name'), third_party_insurer.get('name')]
        for external_party in external_parties:
            names.append(external_party.get('external_party', {}).get('name'))
        names = [name for name in names if name]
        if len(set(names)) != len(names):
            raise serializers.ValidationError('the uniqueness of the names is not respected.')

        if customer:
            try:
                CustomerSerializer(
                    instance=Customer.objects.filter(id=customer.get('id', None)).first(),
                    data=customer
                ).is_valid(raise_exception=True)
            except ValidationError as e:
                raise ValidationError({'customer': e.detail})
        if customer_vehicle := attrs.get('customer_vehicle', {}):
            try:
                VehicleSerializer(
                    instance=Vehicle.objects.filter(
                        id=customer_vehicle.get('id', None),
                        owner=Vehicle.Owner.customer
                    ).first(),
                    data={
                        **customer_vehicle,
                        'owner': Vehicle.Owner.customer
                    }
                ).is_valid(raise_exception=True)
            except ValidationError as e:
                raise ValidationError({'customer_vehicle': e.detail})
        if third_party:
            try:
                ThirdPartySerializer(
                    instance=ThirdParty.objects.filter(id=third_party.get('id', None)).first(),
                    data=third_party
                ).is_valid(raise_exception=True)
            except ValidationError as e:
                raise ValidationError({'third_party': e.detail})
        if self.instance and (injuries := attrs.get('injuries', {})):
            for injury in injuries:
                try:
                    InjuryCaseSerializer(
                        instance=Injury.objects.filter(id=injury.get('id', None)).first(),
                        data={
                            **injury,
                            'case': self.instance.id
                        }
                    ).is_valid(raise_exception=True)
                except ValidationError as e:
                    raise ValidationError({'injuries': e.detail})

        return attrs

    @staticmethod
    def __save_customer(customer_data):
        customer_serializer = CustomerSerializer(
            instance=Customer.objects.filter(id=customer_data.get('id', None)).first(),
            data=customer_data
        )
        try:
            customer_serializer.is_valid(raise_exception=True)
            customer = customer_serializer.save()
        except ValidationError as e:
            raise ValidationError({'customer': e.detail})
        return customer

    @staticmethod
    def __save_customer_vehicle(customer_vehicle_data):
        if not customer_vehicle_data:
            return None

        vehicle_serializer = VehicleSerializer(
            instance=Vehicle.objects.filter(
                id=customer_vehicle_data.get('id', None),
                owner=Vehicle.Owner.customer
            ).first(),
            data={
                **customer_vehicle_data,
                'owner': Vehicle.Owner.customer
            }
        )
        try:
            vehicle_serializer.is_valid(raise_exception=True)
            vehicle = vehicle_serializer.save()
        except ValidationError as e:
            raise ValidationError({'customer_vehicle': e.detail})
        return vehicle

    @staticmethod
    def __save_third_party(third_party_data):
        if not third_party_data:
            return None

        tps = ThirdPartySerializer(
            instance=ThirdParty.objects.filter(id=third_party_data.get('id', None)).first(),
            data=third_party_data
        )
        try:
            tps.is_valid(raise_exception=True)
            tp = tps.save()
        except ValidationError as e:
            raise ValidationError({'third_party': e.detail})
        return tp

    @staticmethod
    def __save_injuries(injuries_data, case_id):
        injuries = []
        for injury in injuries_data:
            injury_serializer = InjuryCaseSerializer(
                instance=Injury.objects.filter(id=injury.get('id', None)).first(),
                data={
                    **injury,
                    'case': case_id
                }
            )

            try:
                injury_serializer.is_valid(raise_exception=True)
                inj = injury_serializer.save()
            except ValidationError as e:
                raise ValidationError({'injuries': e.detail})
            injuries.append(inj)
        return injuries

    @staticmethod
    def __save_external_parties(external_parties_data, case_id):
        for external_party in external_parties_data:
            external_party = external_party.get('external_party', {})

            external_party_object = ExternalParty.objects.update_or_create(
                # Use __exact so id won't be used while creating object
                id__exact=external_party.pop('id', None),
                is_third_party=False,
                defaults=external_party
            )[0] if external_party else None

            if external_party_object:
                ExternalPartyService.objects.get_or_create(external_party=external_party_object, case_id=case_id)

    def create(self, validated_data):
        request = self.context['request']
        worker = request.user

        customer = self.__save_customer(validated_data.pop('customer'))
        customer_vehicle = self.__save_customer_vehicle(validated_data.pop('customer_vehicle', {}))
        third_party = self.__save_third_party(validated_data.pop('third_party'))

        external_parties_data = validated_data.pop('related_external_parties', {})
        injuries_data = validated_data.pop('injuries', [])

        instance = super().create(
            {
                **validated_data,
                'customer': customer,
                'customer_vehicle': customer_vehicle,
                'third_party': third_party,
                'worker': worker
            }
        )

        self.__save_injuries(injuries_data, instance.pk)
        self.__save_external_parties(external_parties_data, instance.pk)

        return instance

    def update(self, instance, validated_data):
        if self.partial:
            Case.objects.filter(pk=instance.pk).update(**validated_data)
            return instance

        customer = self.__save_customer(validated_data.pop('customer'))
        customer_vehicle = self.__save_customer_vehicle(validated_data.pop('customer_vehicle', {}))
        third_party = self.__save_third_party(validated_data.pop('third_party'))
        self.__save_injuries(validated_data.pop('injuries', []), instance.pk)
        self.__save_external_parties(validated_data.pop('related_external_parties', []), instance.pk)

        return super().update(
            instance,
            validated_data={
                **validated_data,
                'customer': customer,
                'customer_vehicle': customer_vehicle,
                'third_party': third_party
            }
        )
