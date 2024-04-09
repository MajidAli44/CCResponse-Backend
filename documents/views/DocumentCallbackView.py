import io

from rest_framework.response import Response
from rest_framework.views import APIView

from common.services.StorageService import storageService
from documents.models import DocumentSignature
from documents.permissions import IsDocusignUser
from documents.services.DocuSignService import docusign_service


class DocumentCallbackView(APIView):
    authentication_classes = ()
    permission_classes = (IsDocusignUser,)

    def post(self, request, *args, **kwargs):
        try:
            document_signature = DocumentSignature.objects.get(envelope_id=request.data.get('envelopeId'))
        except DocumentSignature.DoesNotExist:
            return Response('OK', status=200)
        else:
            document_signature.status = request.data.get('status')
            document_signature.save(update_fields=['status'])

            rel_file_path = docusign_service.download_document(
                envelope_id=document_signature.envelope_id,
                document_id=document_signature.document_id
            )

            storageService.delete_s3(document_signature.document.rel_file_path)
            with open(rel_file_path, 'rb') as fin:
                data = io.BytesIO(fin.read())
                new_rel_file_path = storageService.put_into_s3_from_stream(data, 'documents/signed', f'{document_signature.document.name}.pdf')

            document = document_signature.document
            document.rel_file_path = new_rel_file_path
            document.save()

        return Response('OK', status=200)
