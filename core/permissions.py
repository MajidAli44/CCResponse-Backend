from rest_framework.permissions import BasePermission

from core.models import User


class IsCRMAdminUser(BasePermission):
    message = 'Only Admin user can access APIs'

    def has_permission(self, request, view):
        return request.user.role == User.UserRoles.admin
