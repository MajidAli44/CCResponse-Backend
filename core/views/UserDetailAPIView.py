from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.serializers import UserDetailSerializer


class UserDetailAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer

    def get(self, request, *args, **kwargs):
        return Response(
            self.serializer_class(instance=request.user).data,
            status=status.HTTP_200_OK
        )
