from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from core.models import EmailVerifyRequest
from core.serializers import EmailVerifySerializer
from core.services import UserService

user_service = UserService


class EmailVerifyAPIView(GenericAPIView):
    """ User email verify """
    permission_classes = [AllowAny]
    serializer_class = EmailVerifySerializer

    @swagger_auto_schema(
        responses={
            200: 'Email verified',
            404: 'Token invalid',
            400: 'Validation errors',
        }
    )
    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        valid_data = serializer_data.validated_data
        try:
            user_token = EmailVerifyRequest.objects.get(token=valid_data['token'])
            is_token_valid = user_service.check_token(
                user_token, valid_data['token']
            )

            if is_token_valid:
                user_token.is_verified = True
                user_token.save()
                return Response('Email verified', status=status.HTTP_200_OK)
        except EmailVerifyRequest.DoesNotExist:
            return Response('Token invalid', status=status.HTTP_404_NOT_FOUND)
