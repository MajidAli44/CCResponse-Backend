from django.apps import apps
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.db import models
from django.utils.translation import gettext_lazy as _
from djchoices import DjangoChoices, ChoiceItem

from ccresponse.storage_backends import PrivateMediaStorage
from core.mail import EmailService
from core.managers import CustomUserManager

password_reset_token_generator = PasswordResetTokenGenerator()
email_service = EmailService


class User(AbstractUser):

    class UserRoles(DjangoChoices):
        admin = ChoiceItem('admin', 'Admin')
        user = ChoiceItem('user', 'user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    username = None
    role = models.CharField(max_length=20, choices=UserRoles.choices)
    email = models.CharField(
        _('email address'),
        max_length=255,
        unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(
        upload_to='avatars/', blank=True, null=True,
        storage=PrivateMediaStorage()
    )
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    other_details = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    def reset_password__send_mail(self):
        # TODO: remove circular import
        PasswordResetRequest = apps.get_model('core', 'PasswordResetRequest')
        PasswordResetRequest.objects.filter(
            user=self
        ).delete()

        token = password_reset_token_generator.make_token(self)
        PasswordResetRequest.objects.create(
            token=token,
            user=self
        )

        email_service.send_restore_password_mail(
            self.fullname,
            self.email,
            token
        )

    def reset_password__set_password(self, password):
        self.set_password(password)
        self.save(update_fields=['password'])
        # TODO: remove circular import
        PasswordResetRequest = apps.get_model('core', 'PasswordResetRequest')
        PasswordResetRequest.objects.filter(user=self).delete()
        email_service.send_password_changed_mail(self.fullname, self.email)

    def verify_email__send_mail(self, new_email):
        token = password_reset_token_generator.make_token(self)
        # TODO: remove circular import
        EmailVerifyRequest = apps.get_model('core', 'EmailVerifyRequest')
        user_email_verify, _ = EmailVerifyRequest.objects.get_or_create(
            user=self
        )
        user_email_verify.token = token
        user_email_verify.is_verified = False
        user_email_verify.save()

        email_service.send_email_verify_mail(
            self.fullname,
            new_email,
            token
        )

    def verify_registration__send_mail(self, email):
        token = password_reset_token_generator.make_token(self)
        # TODO: remove circular import
        RegistrationVerifyRequest = apps.get_model('core', 'RegistrationVerifyRequest')
        user_registration_verify, _ = RegistrationVerifyRequest.objects.get_or_create(
            user=self
        )
        user_registration_verify.token = token
        user_registration_verify.is_verified = False
        user_registration_verify.save()

        email_service.send_email_verify_mail(
            self.fullname,
            email,
            token
        )
