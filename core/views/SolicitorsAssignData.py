from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import ExternalParty


class SolicitorsAssignData(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            ExternalParty.objects.filter(role=ExternalParty.Role.solicitor).values('id', 'name'),
            status=status.HTTP_200_OK
        )
