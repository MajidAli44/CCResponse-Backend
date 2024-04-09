from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from common.services.StorageService import storageService
from documents.models import Document
from documents.serializers import DocumentSerializer


class DocumentListAPIView(ListCreateAPIView):

    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DocumentSerializer

    def get_queryset(self):
        case_id = self.request.query_params.get('case_pk')
        introducer_id = self.request.query_params.get('introducer_pk')
        solicitor_id = self.request.query_params.get('solicitor_pk')

        if case_id is not None:
            return Document.objects.filter(case_id=case_id).order_by('name')

        if introducer_id is not None:
            return Document.objects.filter(introducer_id=introducer_id).order_by('name')

        if solicitor_id is not None:
            return Document.objects.filter(solicitor_id=solicitor_id).order_by('name')

        raise Exception('Please input case_id or introducer_id or solicitor_id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user_id = self.request.POST.get('user')
        case_id = self.request.POST.get('case')
        introducer_id = self.request.POST.get('introducer')
        solicitor_id = self.request.POST.get('solicitor')
        filename = self.request.POST.get('filename')
        file = self.request.FILES['file']

        if case_id is not None:
            rel_file_path = storageService.put_into_s3_from_stream(file, f'documents/{case_id}', filename)
            Document.objects.create(user_id=user_id, case_id=case_id, name=filename, rel_file_path=rel_file_path, display_document_in_table=True)
        elif introducer_id is not None:
            rel_file_path = storageService.put_into_s3_from_stream(file, f'documents/{introducer_id}', filename)
            Document.objects.create(user_id=user_id, introducer_id=introducer_id, name=filename, rel_file_path=rel_file_path, display_document_in_table=True)
        elif solicitor_id is not None:
            rel_file_path = storageService.put_into_s3_from_stream(file, f'documents/{solicitor_id}', filename)
            Document.objects.create(user_id=user_id, solicitor_id=solicitor_id, name=filename, rel_file_path=rel_file_path, display_document_in_table=True)
        else:
            return JsonResponse({'status': False})

        return JsonResponse({'status': True})
