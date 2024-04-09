from django.db import IntegrityError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from core.serializers import JWTRefreshTokenSerializer


class UserLogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_id='auth_logout',
        request_body=JWTRefreshTokenSerializer,
        responses={
            200: 'Logged out',
            400: 'Validation error',
            404: 'Token invalid or expired',
        }
    )
    def post(self, request):
        serializer = JWTRefreshTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            token = RefreshToken(serializer.validated_data['refresh_token'])
            token.blacklist()
        except IntegrityError:
            return Response(
                'Token invalid or expired',
                status=status.HTTP_404_NOT_FOUND
            )

        return Response('Logged out', status=status.HTTP_200_OK)
