import io

from django.core.management.base import BaseCommand

from common.services.StorageService import storageService
from documents.models import DocumentSignature
from documents.services.DocuSignService import docusign_service


class Command(BaseCommand):

    def handle(self, *args, **options):

        signatures = DocumentSignature.objects.filter()
        for current_signature in signatures:
            if current_signature.status in [
                DocumentSignature.Statuses.completed, DocumentSignature.Statuses.declined,
                DocumentSignature.Statuses.voided, DocumentSignature.Statuses.deleted
            ]:
                continue

            current_signature.status = docusign_service.get_envelope_status(current_signature.envelope_id)
            current_signature.save(update_fields=['status'])

            if current_signature.status == DocumentSignature.Statuses.completed:
                rel_file_path = docusign_service.download_document(
                    envelope_id=current_signature.envelope_id,
                    document_id=current_signature.document_id
                )

                storageService.delete_s3(current_signature.document.rel_file_path)
                with open(rel_file_path, 'rb') as fin:
                    data = io.BytesIO(fin.read())
                    new_rel_file_path = storageService.put_into_s3_from_stream(data, 'documents/signed',  f'{current_signature.document.name}.pdf')

                document = current_signature.document
                document.rel_file_path = new_rel_file_path
                document.save()
