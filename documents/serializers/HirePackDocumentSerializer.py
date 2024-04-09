from datetime import date
from decimal import Decimal

from django.utils import timezone
from rest_framework import serializers

from cases.models import Case


class HirePackDocumentSerializer(serializers.ModelSerializer):

    current_date = serializers.SerializerMethodField()
    accident_date = serializers.DateField(source='accident.accident_date', allow_null=True)

    client_cc_ref = serializers.CharField(source='cc_ref', allow_null=True)
    client_name = serializers.CharField(source='client.name', allow_null=True)
    client_address = serializers.SerializerMethodField()
    client_phone_number = serializers.CharField(source='client.phone_number', allow_null=True)
    client_date_of_birth = serializers.DateField(source='client.date_of_birth', allow_null=True)
    client_license_number = serializers.CharField(source='client.license_number', allow_null=True)
    client_vrn = serializers.CharField(source='client.vehicle.vrn', allow_null=True)
    client_vehicle_make_model = serializers.SerializerMethodField()

    storage_from = serializers.DateField(source='storage_detail.from_date', allow_null=True)
    storage_to = serializers.DateField(source='storage_detail.end_date', default=timezone.now)
    storage_fee_per_day = serializers.DecimalField(source='storage_detail.fee_per_day', allow_null=True, decimal_places=2, max_digits=12)
    days_in_storage = serializers.IntegerField(source='storage_detail.days_in_storage', allow_null=True)

    recovery_amount = serializers.SerializerMethodField()

    total_storage_amount = serializers.SerializerMethodField()

    # hire_mk = serializers.CharField(source='hire_detail.vehicle.make', allow_null=True)
    # hire_md = serializers.CharField(source='hire_detail.vehicle.model', allow_null=True)
    # hire_vrn = serializers.CharField(source='hire_detail.vehicle.vrn', allow_null=True)
    hire_mk_md = serializers.SerializerMethodField()
    hire_vrn = serializers.SerializerMethodField()
    hire_start_date = serializers.DateField(source='hire_detail.start_date', allow_null=True)
    hire_end_date = serializers.DateField(source='hire_detail.end_date', allow_null=True)
    hire_due_back_date = serializers.DateField(source='hire_detail.due_back_date', allow_null=True)
    hire_charge_per_day = serializers.DecimalField(source='hire_detail.charge', allow_null=True, decimal_places=2, max_digits=12)
    cdw_per_day = serializers.CharField(source='hire_detail.cdw', allow_null=True)

    driver_name = serializers.CharField(source='hire_detail.driver_full_name', allow_null=True)
    driver_license_number = serializers.CharField(source='hire_detail.driver_license_number', allow_null=True)
    driver_dob = serializers.DateField(source='hire_detail.driver_date_of_birth', allow_null=True)

    # Total Max Daily Rate
    tmdr = serializers.SerializerMethodField()
    # Total Max Daily Rate CR
    tmdrc = serializers.SerializerMethodField()

    tp_insurer_ref = serializers.CharField(source='third_party.insurer_ref', allow_null=True)
    tp_name = serializers.SerializerMethodField(allow_null=True)

    prosecution = serializers.BooleanField(source='hire_agreement.prosecution')
    accident_loss_in_3_past_years = serializers.BooleanField(source='hire_agreement.accident_loss_in_3_past_years')
    proposal_declined_or_increased_fees = serializers.BooleanField(source='hire_agreement.proposal_declined_or_increased_fees')
    diseases = serializers.BooleanField(source='hire_agreement.diseases')

    offer_received = serializers.SerializerMethodField()

    extras_total = serializers.SerializerMethodField()

    nsi_age = serializers.SerializerMethodField()
    nsi_occupation = serializers.SerializerMethodField()
    nsi_driving_licence = serializers.SerializerMethodField()
    nsi_convictions_points = serializers.SerializerMethodField()

    class Meta:
        model = Case
        fields = (
            'current_date', 'client_cc_ref', 'client_name', 'tp_insurer_ref', 'tp_name',
            'accident_date', 'client_vrn', 'client_address', 'client_phone_number',
            'client_vehicle_make_model', 'storage_from', 'storage_to', 'storage_fee_per_day', 'days_in_storage',
            'recovery_amount', 'total_storage_amount', 'client_date_of_birth', 'client_license_number',
            'hire_mk_md', 'hire_vrn', 'hire_start_date', 'hire_end_date',
            'hire_charge_per_day', 'cdw_per_day', 'tmdr', 'tmdrc', 'driver_name', 'driver_license_number',
            'driver_dob', 'hire_due_back_date', 'prosecution', 'accident_loss_in_3_past_years',
            'proposal_declined_or_increased_fees', 'diseases', 'offer_received', 'extras_total',
            'nsi_age', 'nsi_occupation', 'nsi_driving_licence', 'nsi_convictions_points',
        )

    def get_current_date(self, _obj):
        return date.today().strftime("%d/%m/%Y")

    def get_total_storage_amount(self, obj):
        total_storage_amount = (obj.storage_detail.days_in_storage or Decimal('0.0')) * (obj.storage_detail.fee_per_day or Decimal('0.0')) + (obj.recovery_detail.recovery_fee or Decimal('0.0')) + (obj.storage_detail.engineers_fee or Decimal('0.0'))
        return total_storage_amount.quantize(Decimal('1.00'))

    def get_tmdr(self, obj):
        return obj.hire_detail.hire_fee_per_day or Decimal('0.00')

    def get_tmdrc(self, obj):
        return ((obj.hire_detail.hire_fee_per_day or Decimal('0.00')) * Decimal('1.3')).quantize(Decimal('1.00'))

    def get_recovery_amount(self, obj):
        total = Decimal('0')
        total += obj.recovery_detail.recovery_fee or Decimal('0.0')
        total += obj.storage_detail.engineers_fee or Decimal('0.0')
        return total.quantize(Decimal('1.00'))

    def get_client_address(self, obj):
        if obj.client:
            if obj.client.address:
                split_address = obj.client.address.split('\n')
                if len(split_address) > 1:
                    if obj.client.postcode:
                        return ', '.join(split_address) + '\n' + obj.client.postcode
                    else:
                        return ', '.join(split_address)
                return obj.client.address + '\n' + obj.client.postcode
        return None

    def get_client_vehicle_make_model(self, obj):
        make_model = ''

        if obj.client.vehicle is not None and obj.client.vehicle.make:
            make_model += obj.client.vehicle.make
        make_model += '/'
        if obj.client.vehicle is not None and obj.client.vehicle.model:
            make_model += obj.client.vehicle.model

        if len(make_model) > 30:
            return make_model[:30]
        return make_model

    def get_hire_mk_md(self, obj):
        if obj.hire_detail.outsourced_vehicle:
            if len(obj.hire_detail.outsourced_vehicle_make_model) > 30:
                return obj.hire_detail.outsourced_vehicle_make_model[:30]
            return obj.hire_detail.outsourced_vehicle_make_model

        make_model = ''
        if obj.hire_detail.vehicle is not None and obj.hire_detail.vehicle.make is not None:
            make_model += obj.hire_detail.vehicle.make
        make_model += '/'
        if obj.hire_detail.vehicle is not None and obj.hire_detail.vehicle.model is not None:
            make_model += obj.hire_detail.vehicle.model

        if len(make_model) > 30:
            return make_model[:30]
        return make_model

    def get_hire_vrn(self, obj):
        if obj.hire_detail.outsourced_vehicle:
            return obj.hire_detail.outsourced_vehicle_vrn

        if obj.hire_detail.vehicle and obj.hire_detail.vehicle.vrn:
            return obj.hire_detail.vehicle.vrn

        return ''

    def get_tp_name(self, obj):
        if obj.third_party:
            if obj.third_party.insurer_ref:
                return obj.third_party.insurer_ref
            elif obj.third_party.vehicle.vrn:
                return obj.third_party.vehicle.vrn
        return ''

    def get_offer_received(self, obj):
        if obj.hire_agreement.offer_received == 'received':
            return 'Yes'
        return 'No'

    def get_extras_total(self, obj):
        extra_total = Decimal('0')
        extra_total += (obj.hire_detail.driver_fee or Decimal('0.0')) if obj.hire_detail.driver_required else Decimal('0.0')
        extra_total += obj.hire_detail.sat_nav or Decimal('0.0')
        extra_total += obj.hire_detail.auto or Decimal('0.0')
        extra_total += obj.hire_detail.towbar or Decimal('0.0')
        extra_total += obj.hire_detail.bluetooth or Decimal('0.0')
        extra_total += obj.hire_detail.ns_driver_fee or Decimal('0.0')
        extra_total *= obj.hire_detail.days_in_hire or Decimal('0.0')
        return extra_total.quantize(Decimal('1.00'))

    def get_nsi_age(self, obj):
        if obj.hire_detail.ns_driver_surcharge:
            return obj.hire_detail.ns_driver_reason == 'age'
        return False
    
    def get_nsi_occupation(self, obj):
        if obj.hire_detail.ns_driver_surcharge:
            return obj.hire_detail.ns_driver_reason == 'occupation'
        return False

    def get_nsi_driving_licence(self, obj):
        if obj.hire_detail.ns_driver_surcharge:
            return obj.hire_detail.ns_driver_reason == 'driving_licence'
        return False
    
    def get_nsi_convictions_points(self, obj):
        if obj.hire_detail.ns_driver_surcharge:
            return obj.hire_detail.ns_driver_reason == 'convictions_points'
        return False
