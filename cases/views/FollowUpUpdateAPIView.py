from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from cases.models import FollowUp
from cases.serializers import FollowUpUpdateSerializer


class FollowUpUpdateAPIView(UpdateAPIView):
    lookup_url_kwarg = 'follow_up_pk'
    http_method_names = ['patch']
    serializer_class = FollowUpUpdateSerializer
    queryset = FollowUp.objects.all()
    permission_classes = (IsAuthenticated,)
