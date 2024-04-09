from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from documents.models import DocumentTemplates
from documents.serializers.DocumentTemplatesSerializer import DocumentTemplatesSerializer
from documents.services import DocumentService


class DocumentTemplatesListAPIView(ListAPIView):

    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DocumentTemplatesSerializer

    def get_queryset(self):
        return DocumentTemplates.objects.filter(case_id=self.request.query_params.get('case_pk')).order_by('name')

    def get(self, request, *args, **kwargs):
        DocumentService.generate_document_templates(self.request.query_params.get('case_pk'))
        return self.list(request, *args, **kwargs)
