from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from documents.models import DocumentSignature
from documents.serializers import DocumentSignatureCreateSerializer
from documents.services.DocuSignService import docusign_service


class DocumentSignatureListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DocumentSignatureCreateSerializer
    queryset = DocumentSignature.objects.all()

    def perform_create(self, serializer):
        document_signature = serializer.save()
        envelope_id = docusign_service.send_via_email(document_signature)
        if envelope_id:
            document_signature.envelope_id = envelope_id
            document_signature.save(update_fields=['envelope_id'])
        else:
            document_signature.delete()
            raise ValidationError({'error': 'Error with send to Docusign'})