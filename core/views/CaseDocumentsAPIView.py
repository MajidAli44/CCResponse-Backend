from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Case, CaseDocument
from core.serializers import CaseDocumentSerializer
from core.utils import PaginatedQSMixin


class CaseDocumentsAPIView(APIView, PaginatedQSMixin):
    case_document_fields = CaseDocument.__dict__.copy()

    def get(self, request, pk, *args, **kwargs):
        case = get_object_or_404(Case.objects.get_queryset(), pk=pk)

        (
            truncated_qs, count, additional_counts,
            old_query_params, page, page_size, _
        ) = self.apply_query_params(request.query_params.copy(), case.documents.all(), self.case_document_fields)
        data = self.build_paginated_response_without_results(request, old_query_params, count, page, page_size)

        data['additional_counts'] = additional_counts
        data['results'] = CaseDocumentSerializer(truncated_qs, many=True).data

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, pk, *args, **kwargs):
        case = get_object_or_404(Case.objects.get_queryset(), pk=pk)

        s = CaseDocumentSerializer(data=request.data, context={'request': request, 'case': case})
        s.is_valid(raise_exception=True)
        instance = s.save()

        return Response(CaseDocumentSerializer(instance).data, status=status.HTTP_201_CREATED)
