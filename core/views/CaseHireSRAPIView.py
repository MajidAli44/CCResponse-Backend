from rest_framework import status
from rest_framework.exceptions import ValidationError as SerializerValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Case, VehicleHire, VehicleStorage, VehicleRecovery, VehicleHireValidation
from core.serializers import CaseVehicleHireSerializer, VehicleHireValidationSerializer, VehicleStorageSerializer, VehicleRecoverySerializer


class CaseHireSRAPIView(APIView):
    @staticmethod
    def create_response_data(hire, hire_validation, storage, recovery):
        return {
            'hire_details': CaseVehicleHireSerializer(hire).data if hire else {},
            'hire_validation': VehicleHireValidationSerializer(hire_validation).data if hire_validation else {},
            'storage_details': VehicleStorageSerializer(storage).data if storage else {},
            'recovery_details': VehicleRecoverySerializer(recovery).data if recovery else {}
        }

    def get(self, request, *args, pk=None, **kwargs):
        case = get_object_or_404(Case.objects.get_queryset(), pk=pk)

        hire = case.hires.all().order_by('created_at').last()
        hire_validation = hire and hire.hire_validation

        storage = case.storages.all().order_by('created_at').last()
        recovery = case.recoveries.all().order_by('created_at').last()

        data = self.create_response_data(hire, hire_validation, storage, recovery)

        return Response(
            data, status=status.HTTP_200_OK
        )

    def put(self, request, *args, pk=None, **kwargs):
        case = get_object_or_404(Case.objects.get_queryset(), pk=pk)
        customer_id = case.customer_id
        data = request.data

        hire_details = data.get('hire_details', None) or {}
        hire_validation_data = data.get('hire_validation', None) or {}
        storage_details = data.get('storage_details', None) or {}
        recovery_details = data.get('recovery_details', None) or {}

        hire_id = hire_details.get('id', None)
        hire_validation_id = hire_validation_data.get('id', None)
        storage_id = storage_details.get('id', None)
        recovery_id = recovery_details.get('id', None)

        hire = VehicleHire.objects.filter(pk=hire_id).first() if hire_id else None
        hire_validation = (
            VehicleHireValidation.objects.filter(pk=hire_validation_id, vehicle_hire_id=hire_id).first()
            if hire_validation_id else None
        )
        storage = VehicleStorage.objects.filter(pk=storage_id, invoice__case_id=pk).first() if storage_id else None
        recovery = VehicleRecovery.objects.filter(pk=recovery_id, invoice__case_id=pk).first() if recovery_id else None

        objs = []
        for data_key, obj_data, obj, s_cls in zip(
                ['hire_details', 'hire_validation', 'storage_details', 'recovery_details'],
                [hire_details, hire_validation_data, storage_details, recovery_details],
                [hire, hire_validation, storage, recovery],
                [CaseVehicleHireSerializer, VehicleHireValidationSerializer,
                 VehicleStorageSerializer, VehicleRecoverySerializer]
        ):
            if obj_data:
                s = s_cls(
                    obj,
                    data={
                        **obj_data,
                        'case': pk,
                        'customer': customer_id
                    }
                )
                try:
                    s.is_valid(raise_exception=True)
                except SerializerValidationError as e:
                    raise SerializerValidationError({data_key: e.detail})

                objs.append(s.save())
            else:
                objs.append(None)

        # pylint: disable=W0632
        hire, hire_validation, storage, recovery = objs

        data = self.create_response_data(hire, hire_validation, storage, recovery)

        return Response(
            data, status=status.HTTP_200_OK
        )

