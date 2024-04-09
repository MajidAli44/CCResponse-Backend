from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from core.models import User
from core.serializers import CreatePasswordSerializer
from core.services import UserService

user_service = UserService


class CreatePasswordAPIView(GenericAPIView):
    """Create password after user was added"""
    permission_classes = [AllowAny]
    serializer_class = CreatePasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        valid_data = serializer_data.validated_data

        try:
            user = User.objects.get(
                registration_verify_request__token=valid_data['token']
            )
            is_token_valid = (user_service.check_token(
                user.registration_verify_request,
                valid_data['token']
            ))
            if is_token_valid:
                user.set_password(valid_data['password'])
                user.save()

                tokens = RefreshToken.for_user(user)

                return Response(
                    {'refresh': str(tokens), 'access': str(tokens.access_token)},
                    status=status.HTTP_200_OK
                )
            return Response(
                'Token invalid or expired',
                status=status.HTTP_404_NOT_FOUND
            )

        except User.DoesNotExist:
            return Response(
                'Token invalid or expired',
                status=status.HTTP_404_NOT_FOUND
            )
