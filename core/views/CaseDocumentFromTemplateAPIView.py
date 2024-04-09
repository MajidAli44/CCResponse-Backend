import io

from django.http import HttpResponse
from docxtpl import DocxTemplate
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.document_template_fields import get_template_context
from core.models import Case, DocumentTemplate


class CaseDocumentFromTemplateAPIView(APIView):

    def post(self, request, pk, *args, **kwargs):
        case = get_object_or_404(Case.objects.get_queryset(), pk=pk)
        document_template_id = request.data.get('document_template_id', None)
        if not document_template_id:
            return Response('document_template_id is not specified', status=status.HTTP_400_BAD_REQUEST)
        try:
            template = DocumentTemplate.objects.get(id=document_template_id)
        except DocumentTemplate.DoesNotExist:
            return Response('Document template with this id does not exist', status=status.HTTP_400_BAD_REQUEST)
        template_context = get_template_context(case)
        tpl = DocxTemplate(template.template_file)
        tpl.render(template_context)
        file_stream = io.BytesIO()
        tpl.save(file_stream)
        file_stream.seek(0)
        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        response['Content-Disposition'] = f'attachment; filename={template.name}.docx'
        response['filename'] = f'{template.name}.docx'
        response['Access-Control-Expose-Headers'] = 'filename'
        response.write(file_stream.read())
        file_stream.close()
        return response
