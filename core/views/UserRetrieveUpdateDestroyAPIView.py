from smtplib import SMTPException

from rest_framework.exceptions import APIException
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from core.models import User
from core.permissions import IsCRMAdminUser
from core.serializers import UserDetailSerializer


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    http_method_names = ['get', 'delete', 'patch']

    def perform_update(self, serializer):
        instance = self.get_object()
        new_email = serializer.validated_data.get('email')
        if instance.email != new_email:
            try:
                instance.verify_email__send_mail(new_email)
            except SMTPException:
                raise APIException('Email sent error')
        serializer.save()

    def get_permissions(self):
        permissions = super().get_permissions()
        if self.request.method in ['DELETE', 'PUT']:
            permissions.append(IsCRMAdminUser())
        return permissions
