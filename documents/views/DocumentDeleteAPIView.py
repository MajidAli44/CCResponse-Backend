from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from documents.models import Document
from documents.serializers import DocumentUploadSerializer


class DocumentDeleteAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DocumentUploadSerializer
    queryset = Document.objects.all()
