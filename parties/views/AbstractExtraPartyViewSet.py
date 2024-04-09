from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.pagination import SmallLimitOffsetPagination


class AbstractExtraPartyViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    pagination_class = SmallLimitOffsetPagination
