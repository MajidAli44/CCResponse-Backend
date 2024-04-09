from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from core.models import PasswordResetRequest
from core.serializers import ResetPwdSetPasswordSerializer


class ResetPasswordSetPasswordAPIView(GenericAPIView):
    """ Set new password """
    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = ResetPwdSetPasswordSerializer

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description='Password changed success response',
                examples={
                    'application/json': {
                        'refresh': 'string',
                        'access': 'string',
                        'message': 'Password changed',
                    }
                }
            ),
            400: 'Password matches the current one',
        }
    )
    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        valid_data = serializer_data.validated_data
        password = valid_data['password']

        password_reset_request = (
            PasswordResetRequest.objects
                .filter(token=valid_data['token'])
                .first()
        )
        user = password_reset_request.user

        try:
            validate_password(password, user)
        except ValidationError as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        if user.check_password(password):
            return Response(
                'Password matches the current one.',
                status=status.HTTP_400_BAD_REQUEST
            )

        user.reset_password__set_password(password)
        token = TokenObtainPairSerializer.get_token(user)

        return Response({
            'refresh': str(token),
            'access': str(token.access_token),
            'message': 'Password changed'
        }, status=status.HTTP_200_OK)
