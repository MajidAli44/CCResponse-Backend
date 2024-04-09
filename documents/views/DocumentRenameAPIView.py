from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from documents.models import Document


class DocumentRenameAPIView(APIView):

    permission_classes = ()
    name_parameter = openapi.Parameter('name', openapi.IN_QUERY, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[name_parameter])
    def patch(self, request, *args, **kwargs):
        document_pk = kwargs.get('document_pk')
        request_data = request.data
        if request_data is None or 'name' not in request_data:
            return JsonResponse({'status': False})

        document = get_object_or_404(Document, pk=document_pk)
        document.name = request_data['name']
        document.save()

        return JsonResponse({'status': True})
