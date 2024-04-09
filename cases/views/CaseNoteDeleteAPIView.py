from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from cases.models import CaseNote


class CaseNoteDeleteAPIView(DestroyAPIView):
    lookup_url_kwarg = 'case_note_pk'
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return CaseNote.objects.filter(case_id=self.kwargs.get('case_pk'))
