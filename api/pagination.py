from rest_framework.pagination import LimitOffsetPagination


class SmallLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 9223372036854775807
