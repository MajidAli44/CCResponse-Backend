from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from cases.models import CaseNote
from cases.serializers import CaseNoteUpdateSerializer


class CaseNoteUpdateAPIView(RetrieveUpdateAPIView):
    lookup_url_kwarg = 'case_note_pk'
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return CaseNoteUpdateSerializer
        return CaseNoteUpdateSerializer

    def get_queryset(self):
        return CaseNote.objects.filter(case_id=self.kwargs.get('case_pk'))
