from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from rest_framework.views import APIView

from common.services.StorageService import storageService
from documents.models import Document


class ZapierDocumentCreateAPIView(APIView):
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        case_id = self.request.POST.get('case_id')
        file = self.request.FILES['file']
        filename = self.request.POST.get('filename')

        if case_id is not None and file is not None and filename is not None:
            rel_file_path = storageService.put_into_s3_from_stream(file, f'documents/{case_id}', filename)
            Document.objects.create(case_id=case_id, name=filename, rel_file_path=rel_file_path, display_document_in_table=True)
            return JsonResponse({'status': True})
        return JsonResponse({'status': False})
