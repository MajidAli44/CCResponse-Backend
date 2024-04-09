from smtplib import SMTPException

from rest_framework import status, filters
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.pagination import SmallLimitOffsetPagination
from core.models import User
from core.permissions import IsCRMAdminUser
from core.serializers import UserSerializer

from core.services import UserService
user_service = UserService


class UserListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsCRMAdminUser)
    queryset = User.objects.all()
    pagination_class = SmallLimitOffsetPagination
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['fullname', 'email']

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        user = User.objects.create_user(
            **validated_data,
            password=user_service.create_random_password()
        )
        try:
            user.verify_registration__send_mail(email=user.email)
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        except SMTPException:
            user.delete()
            return Response(
                'Email sent error', status=status.HTTP_403_FORBIDDEN
            )
