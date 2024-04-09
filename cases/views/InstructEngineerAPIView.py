from smtplib import SMTPException

from django.http import Http404
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cases.models import Case, HireValidation
from core.mail import EmailService


class InstructEngineerAPIView(APIView):
    email_service = EmailService

    def get(self, request, *args, **kwargs):
        try:
            case = Case.objects.get(id=kwargs.get('case_pk'))
        except Case.DoesNotExist:
            raise Http404
        else:
            try:
                self.email_service.send_instruct_engineer_mail()
                hire_validation, _ = HireValidation.objects.get_or_create(case=case)
                hire_validation.engs_instructed = timezone.now()
                hire_validation.save(update_fields=['engs_instructed'])
                return Response('Engineer instructed', status=status.HTTP_200_OK)
            except (SMTPException, AttributeError):
                return Response(
                    'Email sent error', status=status.HTTP_403_FORBIDDEN
                )
