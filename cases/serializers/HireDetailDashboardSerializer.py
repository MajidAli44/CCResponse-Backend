from rest_framework import serializers

from cases.models import HireDetail
from cases.serializers import CaseListSerializer
class HireDetailDashboardSerializer(serializers.ModelSerializer):

    case = serializers.SerializerMethodField()
    client_vehicle_make_model = serializers.CharField(source='case.client.vehicle.make_model', allow_null=True, required=False)

    def get_case(self, obj):
        case_instance = getattr(obj, 'case', None)  # None if not defined
        if case_instance is not None:
            return CaseListSerializer(case_instance).data
        else:
            return None

    class Meta:
        model = HireDetail
        fields = (
            'provider', 'case', 'status', 'vehicle', 'start_date', 'end_date', 'client_vehicle_make_model'

            # , 'outsourced', 'charge', 'collection', 'delivery', 'cdw_required', 'cdw', 'driver_required',
            # 'driver_full_name', 'driver_date_of_birth', 'driver_license_number',
            # 'driver_fee', 'sat_nav', 'auto', 'towbar', 'bluetooth',
            # 'settlement_status', 'hire_fee', 'recovery_fee', 'engineers_fee',
            # 'storage_fee', 'outsourced_vehicle', 'outsourced_vehicle_vrn', 'outsourced_vehicle_make_model',
            # 'outsourced_vehicle_fee', 'ns_driver_surcharge', 'ns_driver_fee', 'ns_driver_reason', 'abi_cat',
            # 'hire_categories'

        )

