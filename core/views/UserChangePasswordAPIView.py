from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.serializers import PasswordChangeSerializer


class UserChangePasswordAPIView(GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        responses={
            200: 'Password changed',
            400: 'Validation error',
            403: 'Current password is incorrect',
        }
    )
    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        validated_data = serializer_data.validated_data
        user = request.user
        if user.check_password(validated_data['current_password']):
            user.set_password(validated_data['new_password'])
            user.save()
            return Response({'message': 'Password changed'}, status=status.HTTP_200_OK)
        return Response({'message': 'Current password is incorrect'}, status=status.HTTP_403_FORBIDDEN)
