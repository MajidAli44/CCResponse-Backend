from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from core.models import Case
from core.serializers import CaseSerializer, CasePartialSerializer


class CaseDetailAPIView(APIView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: CaseSerializer()})
    def get(self, request, *args, pk=None, **kwargs):
        case = get_object_or_404(Case, pk=pk)
        serializer = CaseSerializer(case, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CaseSerializer,
        responses={
            status.HTTP_200_OK: 'Ok',
            status.HTTP_400_BAD_REQUEST: "Bad Request"
        },
        operation_id='case_update',
    )
    def put(self, request, *args, pk=None, **kwargs):
        case = get_object_or_404(Case.objects.all(), id=pk)
        serializer = CaseSerializer(case, data=request.data)

        if serializer.is_valid():
            obj = serializer.save()
            response = Response(status=status.HTTP_200_OK)
            response['Location'] = reverse('cases-detail', kwargs={'pk': obj.id})
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=CasePartialSerializer,
        responses={
            status.HTTP_200_OK: 'Ok',
            status.HTTP_400_BAD_REQUEST: "Bad Request"
        },
        operation_id='case_partial_update',
        operation_description='Partial !Case-only! fields update'
    )
    def patch(self, request, pk=None):
        case = get_object_or_404(Case.objects.all(), id=pk)
        serializer = CasePartialSerializer(case, data=request.data)

        if serializer.is_valid():
            obj = serializer.save()
            response = Response(status=status.HTTP_200_OK)
            response['Location'] = reverse('cases-detail', kwargs={'pk': obj.id})
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
