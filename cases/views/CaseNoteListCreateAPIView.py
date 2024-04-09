from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from cases.models import CaseNote
from cases.serializers import CaseNoteListSerializer, CaseNoteCreateSerializer


class CaseNoteListCreateAPIView(ListCreateAPIView):
    lookup_url_kwarg = 'case_note_pk'
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return CaseNote.objects.filter(case_id=self.kwargs.get('case_pk')).order_by('-created_at')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CaseNoteListSerializer
        return CaseNoteCreateSerializer
