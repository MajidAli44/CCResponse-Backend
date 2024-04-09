from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from core.models import RegistrationVerifyRequest
from core.serializers import RegistrationVerifySerializer
from core.services import UserService


class RegistrationVerifyAPIView(GenericAPIView):
    """ User registration verify """
    permission_classes = [AllowAny]
    serializer_class = RegistrationVerifySerializer

    user_service = UserService

    @swagger_auto_schema(
        responses={
            200: 'Registration verified',
            404: 'Token invalid',
            400: 'Validation errors',
        }
    )
    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        valid_data = serializer_data.validated_data
        try:
            user_token = RegistrationVerifyRequest.objects.get(token=valid_data['token'])
            is_token_valid = self.user_service.check_token(
                user_token, valid_data['token']
            )
            if is_token_valid:
                user_token.is_verified = True
                user_token.save()
                email_verify = user_token.user.email_verify_request
                email_verify.is_verified = True
                email_verify.save()
                return Response('Registration verified', status=status.HTTP_200_OK)
        except RegistrationVerifyRequest.DoesNotExist:
            return Response('Token invalid', status=status.HTTP_404_NOT_FOUND)
