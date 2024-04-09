from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from documents.models import Document
from documents.serializers import DocumentUploadDownloadSerializer, DocumentDownloadResponseSerializer
from documents.services import DocumentService


class DocumentDownloadAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DocumentUploadDownloadSerializer
    queryset = Document.objects.all()
    document_service = DocumentService

    @swagger_auto_schema(
        responses={200: DocumentDownloadResponseSerializer()}
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = self.document_service.get_document_url(
            serializer.validated_data['document_ids']
        )
        return Response(
            DocumentDownloadResponseSerializer({'url': url}).data
        )
