from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.exceptions import UnsupportedMediaType
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.pagination import SmallLimitOffsetPagination
from cases.filters import CaseFilter, CustomOrdering
from cases.models import Case
from cases.serializers import CaseCreateSerializer, CaseListSerializer
from cases.services import CaseService, CaseExportService

case_service = CaseService()


class CaseListCreateAPIView(ListCreateAPIView):
    lookup_url_kwarg = 'case_pk'
    queryset = Case.objects.all()
    export_service = CaseExportService
    permission_classes = (IsAuthenticated,)
    pagination_class = SmallLimitOffsetPagination
    filter_backends = (
        filters.SearchFilter, CustomOrdering, DjangoFilterBackend,
    )
    filterset_class = CaseFilter
    search_fields = (
        'client__name', 'client__phone_number', 'introducer__name', 'third_party__insurer__name', 'services'
    )
    ordering_fields = (
        'created_at', 'accident__accident_date', 'client__name', 'client__phone_number',
        'introducer__name', 'client__notes', 'third_party__insurer__name'
    )

    def _export_document(self):
        return {
            'pdf': self.export_service.export_to_pdf,
            'excel': self.export_service.export_to_excel,
        }

    def list(self, request, *args, **kwargs):

        search_arg = str(self.request.query_params.get('search', '')).lower()
        if len(search_arg.strip()) > 3 and search_arg.startswith('cc/'):
            queryset = self.get_queryset()
        else:
            queryset = self.filter_queryset(self.get_queryset())

        export_format = request.GET.get('export_format')

        if export_format:
            allowed_formats = self._export_document()
            if export_format not in allowed_formats:
                raise UnsupportedMediaType(export_format or 'null')
            return Response({
                'url': allowed_formats.get(export_format)(queryset=queryset)
            }, status=status.HTTP_200_OK)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginated_response = self.get_paginated_response(serializer.data)
            paginated_response.data.update({
                **case_service.get_each_status_count_of_cases()
            })
            return paginated_response

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not request.data.get('file_handler'):
            serializer.save(file_handler=request.user, case_creator=request.user)
        else:
            serializer.save(case_creator=request.user)
        return Response(serializer.data)

    def get_queryset(self):
        # Check for searching by CC Ref because CC Ref is property
        search_arg = str(self.request.query_params.get('search', '')).lower()
        if len(search_arg.strip()) > 3 and search_arg.startswith('cc/'):
            id_for_search = int(search_arg.split('cc/')[1])
            self.queryset = Case.objects.filter(id=id_for_search)
            return self.queryset
        return self.queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CaseListSerializer
        return CaseCreateSerializer
