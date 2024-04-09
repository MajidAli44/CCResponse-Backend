from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Case
from core.serializers import CaseNoteSerializer, CaseNoteCreationSerializer


class CaseNoteAPIView(APIView):

    def get(self, request, *args, pk=None, **kwargs):
        case = get_object_or_404(Case, pk=pk)
        notes = case.case_notes.all()
        serializer = CaseNoteSerializer(notes, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CaseNoteCreationSerializer,
        responses={
            status.HTTP_201_CREATED: 'Created',
            status.HTTP_400_BAD_REQUEST: "Bad Request"
        },
        operation_id='case_note_create',
    )
    def post(self, request, *args, pk=None, **kwargs):
        get_object_or_404(Case, pk=pk)
        serializer = CaseNoteCreationSerializer(data=request.data, context={'request': request, 'case_id': pk})
        if serializer.is_valid():
            obj = serializer.save()
            return Response(data=CaseNoteSerializer(obj).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
