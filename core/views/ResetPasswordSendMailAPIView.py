from smtplib import SMTPException

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from core.models import User
from core.serializers import ResetPwdSendMailSerializer
from core.services import UserService

user_service = UserService


class ResetPasswordSendMailAPIView(GenericAPIView):
    """ Send email for password reset """
    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = ResetPwdSendMailSerializer

    @swagger_auto_schema(
        responses={
            200: 'Email sent successfully',
            404: 'User with specified email not found',
            400: 'Validation errors',
        }
    )
    def post(self, request, *args, **kwargs):

        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        try:
            user = User.objects.get(email=serializer_data.validated_data['email'])
        except User.DoesNotExist:
            return Response(
                'User with specified email not found',
                status=status.HTTP_404_NOT_FOUND
            )
        else:
            try:
                user.reset_password__send_mail()
            except SMTPException:
                raise APIException('Email sent error')
            return Response('Email sent successfully', status=status.HTTP_200_OK)
