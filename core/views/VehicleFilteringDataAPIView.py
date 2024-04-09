from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Customer


class VehicleFilteringDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'customers': Customer.objects.values('id', 'name', 'phone_number'),
        })
