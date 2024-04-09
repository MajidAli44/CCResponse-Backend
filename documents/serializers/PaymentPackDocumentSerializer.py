from datetime import date
from decimal import Decimal

from rest_framework import serializers

from cases.models import Case, CaseFieldsDefaultPrice, RecoveryDetail


class PaymentPackDocumentSerializer(serializers.ModelSerializer):

    current_date = serializers.SerializerMethodField()
    client_cc_ref = serializers.CharField(source='cc_ref')
    client_name = serializers.CharField(source='client.name', allow_null=True)
    client_vrn = serializers.CharField(source='client.vehicle.vrn', allow_null=True)
    accident_date = serializers.DateField(source='accident.accident_date', allow_null=True)
    tp_name = serializers.CharField(source='third_party.name', allow_null=True)
    tp_vrn = serializers.CharField(source='third_party.vehicle.vrn', allow_null=True)
    tp_insurer_ref = serializers.CharField(source='third_party.insurer_ref', allow_null=True)

    date_eng_instructed = serializers.DateField(source='hire_validation.engs_instructed', allow_null=True)
    date_inspection = serializers.DateField(source='hire_validation.inspection_date', allow_null=True)
    date_report_received = serializers.DateField(source='hire_validation.report_received', allow_null=True)
    date_sent_to_tp = serializers.DateField(source='hire_validation.sent_to_tp', allow_null=True)
    date_repair_authorized = serializers.DateField(source='hire_validation.repair_auth', allow_null=True)

    date_settlement_offer = serializers.DateField(source='hire_validation.settle_offer', allow_null=True)
    date_offer_accepted = serializers.DateField(source='hire_validation.offer_accepted', allow_null=True)
    date_cheque_received = serializers.DateField(source='hire_validation.cheque_received', allow_null=True)

    date_satisfaction_signed = serializers.DateField(source='hire_validation.sat_note_sign', allow_null=True)

    storage_from = serializers.DateField(source='storage_detail.from_date', allow_null=True)
    storage_to = serializers.DateField(source='storage_detail.end_date', allow_null=True)
    storage_fee_per_day = serializers.SerializerMethodField()
    days_in_storage = serializers.DecimalField(source='storage_detail.days_in_storage', allow_null=True, decimal_places=2, max_digits=12)
    storage_total_sum = serializers.DecimalField(source='storage_detail.storage_total_sum', allow_null=True, decimal_places=2, max_digits=12)
    storage_total_sum_vat = serializers.SerializerMethodField()

    recovery_type = serializers.SerializerMethodField(allow_null=True)

    recovery_call_out_charge = serializers.SerializerMethodField()
    recovery_call_out_charge_vat = serializers.SerializerMethodField()

    engineer_fee = serializers.SerializerMethodField()
    engineer_fee_vat = serializers.SerializerMethodField()

    winching_time = serializers.SerializerMethodField()
    winching_time_type = serializers.SerializerMethodField()
    winching_time_vat = serializers.SerializerMethodField()

    road_cleanup = serializers.SerializerMethodField()
    road_cleanup_vat = serializers.SerializerMethodField()

    skates_total_sum = serializers.SerializerMethodField()
    skates_total_sum_vat = serializers.SerializerMethodField()

    inherited_fees = serializers.SerializerMethodField()
    inherited_fees_vat = serializers.SerializerMethodField()

    storage_total_net = serializers.SerializerMethodField()
    storage_total_vat = serializers.SerializerMethodField()
    storage_total = serializers.SerializerMethodField()
    storage_total_lt15 = serializers.SerializerMethodField()
    storage_total_gt15 = serializers.SerializerMethodField()
    storage_total_gt30 = serializers.SerializerMethodField()

    # hire_vehicle_make = serializers.CharField(source='hire_detail.vehicle.make', allow_null=True)
    # hire_vehicle_model = serializers.CharField(source='hire_detail.vehicle.model', allow_null=True)
    # hire_vrn = serializers.CharField(source='hire_detail.vehicle.vrn', allow_null=True)
    hire_vehicle_make = serializers.SerializerMethodField()
    hire_vehicle_model = serializers.SerializerMethodField()
    hire_vrn = serializers.SerializerMethodField()
    hire_start_date = serializers.DateField(source='hire_detail.start_date', allow_null=True)
    hire_end_date = serializers.DateField(source='hire_detail.end_date', allow_null=True)
    hire_charge_per_day = serializers.SerializerMethodField()
    days_in_hire = serializers.IntegerField(source='hire_detail.days_in_hire', allow_null=True)

    hire_total_sum = serializers.SerializerMethodField()
    hire_total_sum_vat = serializers.SerializerMethodField()

    delivery_charge = serializers.DecimalField(source='hire_detail.delivery',  allow_null=True, decimal_places=2, max_digits=12)
    delivery_charge_vat = serializers.SerializerMethodField()

    collection_charge = serializers.DecimalField(source='hire_detail.collection', allow_null=True, decimal_places=2, max_digits=12)
    collection_charge_vat = serializers.SerializerMethodField()

    abi_admin_fee = serializers.SerializerMethodField()
    abi_admin_fee_vat = serializers.SerializerMethodField()

    cdw_per_day = serializers.DecimalField(source='hire_detail.cdw', allow_null=True, decimal_places=2, max_digits=12)
    additional_driver = serializers.DecimalField(source='hire_detail.driver_fee', allow_null=True, decimal_places=2, max_digits=12)
    sat_nav = serializers.DecimalField(source='hire_detail.sat_nav', allow_null=True, decimal_places=2, max_digits=12)
    auto = serializers.DecimalField(source='hire_detail.auto', allow_null=True, decimal_places=2, max_digits=12)
    towbar = serializers.DecimalField(source='hire_detail.towbar', allow_null=True, decimal_places=2, max_digits=12)
    bluetooth = serializers.DecimalField(source='hire_detail.bluetooth', allow_null=True, decimal_places=2, max_digits=12)
    ns_driver_surcharge = serializers.DecimalField(source='hire_detail.ns_driver_fee', allow_null=True, decimal_places=2, max_digits=12)

    extras_total = serializers.SerializerMethodField()
    extras_total_vat = serializers.SerializerMethodField()

    hire_total_net = serializers.SerializerMethodField()
    hire_total_vat = serializers.SerializerMethodField()
    hire_total = serializers.SerializerMethodField()
    hire_total_lt15 = serializers.SerializerMethodField()
    hire_total_gt15 = serializers.SerializerMethodField()
    hire_total_gt30 = serializers.SerializerMethodField()

    pay_pack_total_net = serializers.SerializerMethodField()
    pay_pack_vat = serializers.SerializerMethodField()
    pay_pack_total = serializers.SerializerMethodField()

    pay_pack_vat_lt15 = serializers.SerializerMethodField()
    pay_pack_total_lt15 = serializers.SerializerMethodField()

    pay_pack_vat_gt15 = serializers.SerializerMethodField()
    pay_pack_total_gt15 = serializers.SerializerMethodField()

    pay_pack_vat_gt30 = serializers.SerializerMethodField()
    pay_pack_total_gt30 = serializers.SerializerMethodField()

    class Meta:
        model = Case
        fields = (
            'current_date', 'client_cc_ref', 'client_name', 'client_vrn', 'accident_date', 'tp_name', 'tp_vrn',
            'tp_insurer_ref', 'date_eng_instructed', 'date_inspection', 'date_report_received', 'date_sent_to_tp',
            'date_repair_authorized', 'date_settlement_offer', 'date_offer_accepted', 'date_cheque_received',
            'date_satisfaction_signed', 'storage_from', 'storage_to', 'storage_fee_per_day', 'days_in_storage',
            'recovery_call_out_charge', 'recovery_call_out_charge_vat', 'engineer_fee', 'engineer_fee_vat',
            'winching_time', 'winching_time_vat', 'road_cleanup', 'road_cleanup_vat', 'skates_total_sum',
            'skates_total_sum_vat', 'inherited_fees', 'inherited_fees_vat', 'storage_total_sum',
            'storage_total_sum_vat', 'storage_total_net', 'storage_total_vat', 'storage_total', 'storage_total_lt15',
            'storage_total_gt15', 'storage_total_gt30', 'hire_vehicle_make', 'hire_vehicle_model', 'hire_vrn',
            'hire_start_date', 'hire_end_date', 'hire_charge_per_day', 'days_in_hire', 'hire_total_sum',
            'hire_total_sum_vat', 'delivery_charge', 'delivery_charge_vat', 'collection_charge',
            'collection_charge_vat', 'cdw_per_day', 'additional_driver', 'sat_nav', 'auto', 'towbar', 'bluetooth',
            'ns_driver_surcharge', 'extras_total', 'extras_total_vat', 'hire_total_net', 'hire_total_vat',
            'hire_total', 'hire_total_lt15', 'hire_total_gt15', 'hire_total_gt30', 'abi_admin_fee', 'abi_admin_fee_vat',
            'winching_time_type', 'pay_pack_total_net', 'pay_pack_vat', 'pay_pack_total', 'pay_pack_vat_lt15',
            'pay_pack_total_lt15', 'pay_pack_vat_gt15', 'pay_pack_total_gt15', 'pay_pack_vat_gt30',
            'pay_pack_total_gt30', 'recovery_type'
        )

    @property
    def default_prices(self):
        return CaseFieldsDefaultPrice.objects.first()

    def get_hire_charge_per_day(self, obj):
        if obj.hire_detail.charge is not None:
            return obj.hire_detail.charge.quantize(Decimal('0.00'))
        return Decimal('0.00')

    def get_storage_fee_per_day(self, obj):
        if obj.storage_detail.fee_per_day is not None:
            return obj.storage_detail.fee_per_day.quantize(Decimal('0.00'))
        return Decimal('0.00')

    def get_inherited_fees(self, obj):
        if obj.recovery_detail.inherited_fees is not None:
            return obj.recovery_detail.inherited_fees.quantize(Decimal('0.00'))
        return Decimal('0.00')

    def get_recovery_call_out_charge(self, obj):
        if obj.recovery_detail.call_out_charge is not None:
            return obj.recovery_detail.call_out_charge.quantize(Decimal('0.00'))
        return Decimal('0.00')

    def get_engineer_fee(self, obj):
        if obj.storage_detail.engineers_fee is not None:
            return obj.storage_detail.engineers_fee.quantize(Decimal('0.00'))
        return Decimal('0.00')

    def get_current_date(self, _):
        return date.today().strftime("%d/%m/%Y")

    def get_recovery_call_out_charge_vat(self, obj):
        return ((obj.recovery_detail.call_out_charge or 0) * Decimal('.2')).quantize(Decimal('1.00'))

    def get_engineer_fee_vat(self, obj):
        return ((obj.storage_detail.engineers_fee or 0) * Decimal('.2')).quantize(Decimal('1.00'))

    def get_winching_time(self, obj):
        if obj.recovery_detail.winching_time == RecoveryDetail.WinchingTimes.minutes_30:
            return self.default_prices.recovery_detail_minutes_30
        elif obj.recovery_detail.winching_time == RecoveryDetail.WinchingTimes.hour_1:
            return self.default_prices.recovery_detail_hour_1
        return Decimal('0.00')

    def get_winching_time_type(self, obj):
        if obj.recovery_detail.winching_time in ['', None]:
            return 'Not selected'
        return dict(RecoveryDetail.WinchingTimes.choices)[obj.recovery_detail.winching_time]

    def get_winching_time_vat(self, obj):
        if obj.recovery_detail.winching_time == RecoveryDetail.WinchingTimes.minutes_30:
            return (self.default_prices.recovery_detail_minutes_30 * Decimal('0.2')).quantize(Decimal('1.00'))
        elif obj.recovery_detail.winching_time == RecoveryDetail.WinchingTimes.hour_1:
            return (self.default_prices.recovery_detail_hour_1 * Decimal('0.2')).quantize(Decimal('1.00'))
        return Decimal('0')

    def get_road_cleanup(self, obj):
        if obj.recovery_detail and obj.recovery_detail.road_cleanup:
            return self.default_prices.recovery_detail_road_cleanup
        return Decimal('0.00')

    def get_road_cleanup_vat(self, obj):
        if obj.recovery_detail and obj.recovery_detail.road_cleanup:
            return self.default_prices.recovery_detail_road_cleanup * Decimal('.2')
        return Decimal('0.00')

    def get_skates_total_sum(self, obj):
        if obj.recovery_detail.skates == RecoveryDetail.Skates.one:
            return self.default_prices.hire_detail_one_fee_for_skates
        elif obj.recovery_detail.skates == RecoveryDetail.Skates.two:
            return self.default_prices.hire_detail_one_fee_for_skates * Decimal('2')
        elif obj.recovery_detail.skates == RecoveryDetail.Skates.three:
            return self.default_prices.hire_detail_one_fee_for_skates * Decimal('3')
        elif obj.recovery_detail.skates == RecoveryDetail.Skates.four:
            return self.default_prices.hire_detail_one_fee_for_skates * Decimal('4')
        elif obj.recovery_detail.skates == RecoveryDetail.Skates.five:
            return self.default_prices.hire_detail_one_fee_for_skates * Decimal('5')
        return Decimal('0.00')

    def get_skates_total_sum_vat(self, obj):
        if obj.recovery_detail.skates == RecoveryDetail.Skates.one:
            return (self.default_prices.hire_detail_one_fee_for_skates * Decimal('.2')).quantize(Decimal('1.00'))
        elif obj.recovery_detail.skates == RecoveryDetail.Skates.two:
            return (self.default_prices.hire_detail_one_fee_for_skates * Decimal('2') * Decimal('.2')).quantize(Decimal('1.00'))
        elif obj.recovery_detail.skates == RecoveryDetail.Skates.three:
            return (self.default_prices.hire_detail_one_fee_for_skates * Decimal('3') * Decimal('.2')).quantize(Decimal('1.00'))
        elif obj.recovery_detail.skates == RecoveryDetail.Skates.four:
            return (self.default_prices.hire_detail_one_fee_for_skates * Decimal('4') * Decimal('.2')).quantize(Decimal('1.00'))
        elif obj.recovery_detail.skates == RecoveryDetail.Skates.five:
            return (self.default_prices.hire_detail_one_fee_for_skates * Decimal('5') * Decimal('.2')).quantize(Decimal('1.00'))
        return Decimal('0')

    def get_inherited_fees_vat(self, obj):
        return ((obj.recovery_detail.inherited_fees or Decimal('0.00')) * Decimal('0.2')).quantize(Decimal('1.00'))

    def get_storage_total_sum_vat(self, obj):
        return ((obj.storage_detail.storage_total_sum or 0) * Decimal('0.2')).quantize(Decimal('1.00'))

    def get_storage_total_net(self, obj):
        total_net = Decimal('0')
        total_net += obj.recovery_detail.call_out_charge or Decimal('0.0')
        total_net += obj.storage_detail.engineers_fee or Decimal('0.0')

        if obj.recovery_detail.winching_time == RecoveryDetail.WinchingTimes.minutes_30:
            total_net += self.default_prices.recovery_detail_minutes_30 or Decimal('0.0')
        elif obj.recovery_detail.winching_time == RecoveryDetail.WinchingTimes.hour_1:
            total_net += self.default_prices.recovery_detail_hour_1 or Decimal('0.0')

        if obj.recovery_detail and obj.recovery_detail.road_cleanup:
            total_net += self.default_prices.recovery_detail_road_cleanup

        if obj.recovery_detail.skates == RecoveryDetail.Skates.one:
            total_net += self.default_prices.hire_detail_one_fee_for_skates
        elif obj.recovery_detail.skates == RecoveryDetail.Skates.two:
            total_net += self.default_prices.hire_detail_one_fee_for_skates * Decimal('2')
        elif obj.recovery_detail.skates == RecoveryDetail.Skates.three:
            total_net += self.default_prices.hire_detail_one_fee_for_skates * Decimal('3')
        elif obj.recovery_detail.skates == RecoveryDetail.Skates.four:
            total_net += self.default_prices.hire_detail_one_fee_for_skates * Decimal('4')
        elif obj.recovery_detail.skates == RecoveryDetail.Skates.five:
            total_net += self.default_prices.hire_detail_one_fee_for_skates * Decimal('5')

        total_net += obj.recovery_detail.inherited_fees or Decimal('0.0')
        total_net += obj.storage_detail.storage_total_sum or Decimal('0.0')

        return total_net.quantize(Decimal('1.00'))

    def get_storage_total_vat(self, obj):
        return (self.get_storage_total_net(obj) * Decimal('0.2')).quantize(Decimal('1.00'))

    def get_storage_total(self, obj):
        return (self.get_storage_total_net(obj) + self.get_storage_total_vat(obj)).quantize(Decimal('1.00'))

    def get_storage_total_lt15(self, obj):
        return (self.get_storage_total(obj) * Decimal('0.85')).quantize(Decimal('1.00'))

    def get_storage_total_gt15(self, obj):
        return (self.get_storage_total(obj) * Decimal('1.15')).quantize(Decimal('1.00'))

    def get_storage_total_gt30(self, obj):
        return (self.get_storage_total(obj) * Decimal('1.30')).quantize(Decimal('1.00'))

    def get_hire_total_sum(self, obj):
        return ((obj.hire_detail.charge or Decimal('0.0')) * (obj.hire_detail.days_in_hire or Decimal('0.0'))).quantize(Decimal('1.00'))

    def get_hire_total_sum_vat(self, obj):
        return (self.get_hire_total_sum(obj) * Decimal('0.2')).quantize(Decimal('1.00'))

    def get_delivery_charge_vat(self, obj):
        return ((obj.hire_detail.delivery or Decimal('0.0')) * Decimal('0.2')).quantize(Decimal('1.00'))

    def get_collection_charge_vat(self, obj):
        return ((obj.hire_detail.collection or Decimal('0.0')) * Decimal('0.2')).quantize(Decimal('1.00'))

    def get_extras_total(self, obj):
        extra_total = Decimal('0')
        extra_total += obj.hire_detail.cdw or Decimal('0.0')
        extra_total += (obj.hire_detail.driver_fee or Decimal('0.0')) if obj.hire_detail.driver_required else Decimal('0.0')
        extra_total += obj.hire_detail.sat_nav or Decimal('0.0')
        extra_total += obj.hire_detail.auto or Decimal('0.0')
        extra_total += obj.hire_detail.towbar or Decimal('0.0')
        extra_total += obj.hire_detail.bluetooth or Decimal('0.0')
        extra_total += obj.hire_detail.ns_driver_fee or Decimal('0.0')
        extra_total *= obj.hire_detail.days_in_hire or Decimal('0.0')
        return extra_total.quantize(Decimal('1.00'))

    def get_extras_total_vat(self, obj):
        return (self.get_extras_total(obj) * Decimal('0.2')).quantize(Decimal('1.00'))

    def get_hire_total_net(self, obj):
        total_net = Decimal('0')
        total_net += self.get_hire_total_sum(obj)
        total_net += obj.hire_detail.delivery or 0
        total_net += obj.hire_detail.collection or 0
        total_net += self.get_abi_admin_fee(obj)
        total_net += self.get_extras_total(obj)
        return total_net.quantize(Decimal('1.00'))

    def get_hire_total_vat(self, obj):
        return (self.get_hire_total_net(obj) * Decimal('0.2')).quantize(Decimal('1.00'))

    def get_hire_total(self, obj):
        total = Decimal('0.0')
        total += self.get_hire_total_net(obj)
        total += self.get_hire_total_vat(obj)
        return total.quantize(Decimal('1.00'))

    def get_hire_total_lt15(self, obj):
        return (self.get_hire_total(obj) * Decimal('0.85')).quantize(Decimal('1.00'))

    def get_hire_total_gt15(self, obj):
        return (self.get_hire_total(obj) * Decimal('1.15')).quantize(Decimal('1.00'))

    def get_hire_total_gt30(self, obj):
        return (self.get_hire_total(obj) * Decimal('1.30')).quantize(Decimal('1.00'))

    def get_abi_admin_fee(self, obj):
        if obj.hire_detail.days_in_hire > 0:
            return Decimal(45.0).quantize(Decimal('1.00'))
        return Decimal('0.00')

    def get_abi_admin_fee_vat(self, _):
        return (self.get_abi_admin_fee(_) * Decimal(.2)).quantize(Decimal('1.00'))

    def get_pay_pack_total_net(self, obj):
        total_net = Decimal(0)
        total_net += self.get_hire_total_net(obj)
        total_net += self.get_storage_total_net(obj)
        return total_net.quantize(Decimal('1.00'))

    def get_pay_pack_vat(self, obj):
        return (self.get_pay_pack_total_net(obj) * Decimal('0.2')).quantize(Decimal('1.00'))

    def get_pay_pack_total(self, obj):
        return (self.get_pay_pack_vat(obj) + self.get_pay_pack_total_net(obj)).quantize(Decimal('1.00'))

    def get_pay_pack_vat_lt15(self, obj):
        return (self.get_pay_pack_vat(obj) * Decimal('0.85')).quantize(Decimal('1.00'))

    def get_pay_pack_total_lt15(self, obj):
        return (self.get_pay_pack_total(obj) * Decimal('0.85')).quantize(Decimal('1.00'))

    def get_pay_pack_vat_gt15(self, obj):
        return (self.get_pay_pack_vat(obj) * Decimal('1.15')).quantize(Decimal('1.00'))

    def get_pay_pack_total_gt15(self, obj):
        return (self.get_pay_pack_total(obj) * Decimal('1.15')).quantize(Decimal('1.00'))

    def get_pay_pack_vat_gt30(self, obj):
        return (self.get_pay_pack_vat(obj) * Decimal('1.30')).quantize(Decimal('1.00'))

    def get_pay_pack_total_gt30(self, obj):
        return (self.get_pay_pack_total(obj) * Decimal('1.30')).quantize(Decimal('1.00'))

    def get_hire_vehicle_make(self, obj):
        if obj.hire_detail.outsourced_vehicle:
            return obj.hire_detail.outsourced_vehicle_make_model.split('/')[0]

        if obj.hire_detail.vehicle and obj.hire_detail.vehicle.make:
            return obj.hire_detail.vehicle.make

        return ''

    def get_hire_vehicle_model(self, obj):
        if obj.hire_detail.outsourced_vehicle:
            split = obj.hire_detail.outsourced_vehicle_make_model.split('/')
            return split[1] if len(split) >= 2 else ''

        if obj.hire_detail.vehicle and obj.hire_detail.vehicle.model:
            return obj.hire_detail.vehicle.model

        return ''

    def get_hire_vrn(self, obj):
        if obj.hire_detail.outsourced_vehicle:
            return obj.hire_detail.outsourced_vehicle_vrn

        if obj.hire_detail.vehicle and obj.hire_detail.vehicle.vrn:
            return obj.hire_detail.vehicle.vrn

        return ''

    def get_recovery_type(self, obj):
        if obj.recovery_detail.recovery_type:
            if obj.recovery_detail.recovery_type == RecoveryDetail.RecoveryTypes.other and \
                obj.recovery_detail.other_recovery_reason is not None and \
                    len(obj.recovery_detail.other_recovery_reason) > 0:
                return obj.recovery_detail.other_recovery_reason
            return RecoveryDetail.RecoveryTypes.values[obj.recovery_detail.recovery_type]
        return ''
