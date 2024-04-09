from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Customer


# Assign data
class CustomersAssignData(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            Customer.objects.values('id', 'name'),
            status=status.HTTP_200_OK
        )
