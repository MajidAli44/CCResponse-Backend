import base64

from rest_framework.authentication import get_authorization_header
from rest_framework.permissions import BasePermission

from ccresponse import settings


class IsDocusignUser(BasePermission):

    def has_permission(self, request, view):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b'basic':
            return False

        auth_decoded = base64.b64decode(auth[1]).decode('utf-8')
        username, password = auth_decoded.split(':')
        return username == settings.DOCUSIGN_USERNAME and password == settings.DOCUSIGN_PASSWORD
