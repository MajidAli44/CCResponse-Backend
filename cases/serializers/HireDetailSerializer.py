from rest_framework import serializers

from cases.models import HireDetail


class HireDetailSerializer(serializers.ModelSerializer):
    total_hire_fee = serializers.ReadOnlyField(source="get_total_hire_fee", allow_null=True)

    class Meta:
        model = HireDetail
        fields = (
            'provider', 'status', 'vehicle', 'start_date', 'end_date', 'outsourced', 'charge',
            'collection', 'delivery', 'cdw_required', 'cdw', 'driver_required',
            'driver_full_name', 'driver_date_of_birth', 'driver_license_number',
            'driver_fee', 'sat_nav', 'auto', 'towbar', 'bluetooth',
            'settlement_status', 'hire_fee', 'recovery_fee', 'engineers_fee',
            'storage_fee', 'outsourced_vehicle', 'outsourced_vehicle_vrn', 'outsourced_vehicle_make_model',
            'outsourced_vehicle_fee', 'ns_driver_surcharge', 'ns_driver_fee', 'ns_driver_reason', 'abi_cat',
            'hire_categories', 'total_hire_fee'
        )

