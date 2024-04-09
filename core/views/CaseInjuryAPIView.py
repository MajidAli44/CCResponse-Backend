from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Case
from core.serializers import InjurySerializer


class CaseInjuryAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        case = get_object_or_404(Case, pk=pk)
        last_injury = case.injuries.order_by('created_at').last()
        data = InjurySerializer(last_injury).data if last_injury else {}
        return Response(data, status=status.HTTP_200_OK)
