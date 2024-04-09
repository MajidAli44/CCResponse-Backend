from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cases.models import UserDisplayCaseColumn
from cases.serializers import UserDisplayCaseColumnSerializer

from cases.services import CaseService

case_service = CaseService()


class UserDisplayCaseColumnCreateAPIView(GenericAPIView):
    serializer_class = UserDisplayCaseColumnSerializer
    queryset = UserDisplayCaseColumn.objects.all()
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial
        )
        serializer.initial_data['columns'] = set(serializer.initial_data['columns'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            # pylint: disable=W0212
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return Response(
            self.get_serializer(self.get_object()).data
        )

    def get_object(self):
        return case_service.get_user_display_columns(self.request.user)

