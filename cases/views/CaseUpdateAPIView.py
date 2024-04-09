from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from cases.models import Case
from cases.serializers import CaseDetailSerializer, CaseUpdateSerializer


class CaseUpdateAPIView(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'case_pk'
    http_method_names = ['patch', 'get', 'delete']
    queryset = Case.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return CaseUpdateSerializer
        return CaseDetailSerializer
