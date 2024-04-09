from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.core.mail import get_connection, send_mail
from django.utils.html import strip_tags


class EmailService:
    """ Sending email messages service """

    _mail_from = settings.DEFAULT_FROM_EMAIL
    _frontend_url = settings.FRONTEND_URL

    @classmethod
    def _send_html_email(cls, subject, recipients, template, context=None):
        html_message = render_to_string(template, context=context)
        plain_message = strip_tags(html_message)
        mail.send_mail(
            subject=subject,
            from_email=cls._mail_from,
            message=plain_message,
            recipient_list=recipients,
            html_message=html_message,
        )

    @classmethod
    def send_restore_password_mail(cls, user_fullname, user_email, token):
        context = {
            'username': user_fullname,
            'link': f'{cls._frontend_url}{settings.FRONTEND_FORGOT_PASSWORD_PATH}'
                    f'?token={token}'
        }
        cls._send_html_email(
            subject='CCResponse. Password Restore',
            recipients=[user_email],
            template='email/password_restore.html',
            context=context,
        )

    @classmethod
    def send_email_verify_mail(cls, user_fullname, user_email, token):
        context = {
            'username': user_fullname,
            'link': f'{cls._frontend_url}{settings.FRONTEND_EMAIL_VERIFY_PATH}'
                    f'{token}'
        }
        cls._send_html_email(
            subject='CCResponse. Email Verify.',
            recipients=[user_email],
            template='email/email_verify.html',
            context=context,
        )

    @classmethod
    def send_registration_verify_mail(cls, user_fullname, user_email, token):
        context = {
            'username': user_fullname,
            'link': f'{cls._frontend_url}'
                    f'{settings.FRONTEND_REGISTRATION_VERIFY_PATH}'
                    f'{token}'
        }
        cls._send_html_email(
            subject='CCResponse. Registration verify.',
            recipients=[user_email],
            template='email/registration_verify.html',
            context=context,
        )

    @classmethod
    def send_password_changed_mail(cls, user_fullname, user_email):
        cls._send_html_email(
            subject='Account password changed',
            recipients=[user_email],
            template='email/password_changed.html',
            context={'username': user_fullname, },
        )

    @classmethod
    def send_instruct_engineer_mail(cls):
        from core.models import InstructEngineer
        cls._send_html_email(
            subject='Instruct engineer email',
            recipients=[InstructEngineer.objects.last().email],
            template='email/instruct_case_engineer.html',
        )


class ReportService:
    _host = settings.REPORT_EMAIL_HOST
    _port = settings.REPORT_EMAIL_PORT
    _username = settings.REPORT_EMAIL_HOST_USER
    _password = settings.REPORT_EMAIL_HOST_PASSWORD
    _use_tls = settings.REPORT_EMAIL_USE_TLS
    _mail_from = settings.REPORT_DEFAULT_FROM_EMAIL

    @classmethod
    def _send_html_email(cls, subject, recipients, template, context=None):
        html_message = render_to_string(template, context=context)
        plain_message = strip_tags(html_message)
        with get_connection(
            host=cls._host,
            port=cls._port,
            username=cls._username,
            password=cls._password,
            use_tls=cls._use_tls,
        ) as email_connection:
            send_mail(
                subject=subject,
                from_email=cls._mail_from,
                message=plain_message,
                recipient_list=recipients,
                html_message=html_message,
                connection=email_connection,
            )
    
    @classmethod
    def send_report_mail(cls, report_title, recipients, cases):
        context = {
            'export_cases': cases,
        }
        cls._send_html_email(
            subject=report_title,
            recipients=recipients,
            template='export_pdf.html',
            context=context,
        )
