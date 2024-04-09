from dateutil import parser
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Case, ScheduledToChaseCase
from core.serializers import ScheduledToChaseCaseSerializer


class ScheduledToChaseCaseSetAPIView(APIView):
    def post(self, request, case_id, *args, **kwargs):
        get_object_or_404(Case.objects.all(), id=case_id)

        chase_date_str = request.data.get('chase_date', None)
        if not chase_date_str:
            return Response('Chase date is not specified', status=status.HTTP_400_BAD_REQUEST)

        try:
            chase_date = parser.parse(chase_date_str).date()
        except parser.ParserError:
            return Response('Chase date has wrong format', status=status.HTTP_400_BAD_REQUEST)

        scheduled_case = ScheduledToChaseCase.objects.update_or_create(
            case_id=case_id,
            defaults={
                'chase_date': chase_date,
                'user_last_scheduled': request.user
            }
        )[0]

        return Response(ScheduledToChaseCaseSerializer(scheduled_case).data, status=status.HTTP_200_OK)
