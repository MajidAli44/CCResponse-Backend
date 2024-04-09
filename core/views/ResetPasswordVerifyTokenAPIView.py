from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from core.serializers import ResetPwdTokenVerifySerializer


class ResetPasswordVerifyTokenAPIView(GenericAPIView):
    """ Verify password reset token """
    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = ResetPwdTokenVerifySerializer

    @swagger_auto_schema(
        responses={
            200: 'Token verified',
            400: 'Validation errors',
        }
    )
    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid(raise_exception=True)

        return Response('Token verified', status=status.HTTP_200_OK)
