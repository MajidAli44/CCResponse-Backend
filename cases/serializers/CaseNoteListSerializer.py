from core.serializers import UserShortInfoSerializer

from .CaseNoteCreateSerializer import CaseNoteCreateSerializer


class CaseNoteListSerializer(CaseNoteCreateSerializer):
    user = UserShortInfoSerializer(required=False, allow_null=True)
