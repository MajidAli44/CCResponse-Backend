from rest_framework.viewsets import ModelViewSet

from core.models import CaseDocument
from core.serializers import CaseDocumentSerializer
from core.utils import PaginatedQSMixin


class CaseDocumentViewSet(ModelViewSet, PaginatedQSMixin):
    serializer_class = CaseDocumentSerializer
    case_document_fields = CaseDocument.__dict__.copy()

    def get_queryset(self):
        return CaseDocument.objects.get_queryset()

    def list(self, request, *args, **kwargs):
        return self.default_list(self.case_document_fields, request, *args, **kwargs)
