from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from documents.models import Document, DocumentTemplates
from documents.serializers import DocumentSelectSerializer, DocumentSerializer
from documents.services import DocumentService


class DocumentSelectAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DocumentSelectSerializer
    queryset = Document.objects.all()

    def get(self, request, *args, **kwargs):

        template = DocumentTemplates.objects.get(id=kwargs.get('pk'))
        generated_document = DocumentService.generate_document(template.case_id, template.template_name)

        return JsonResponse(DocumentSerializer(generated_document).data)

