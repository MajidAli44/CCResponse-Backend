from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from core.models import User
from core.serializers import UserPublicSerializer


class UserListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
