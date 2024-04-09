from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Case, Chat
from core.serializers import ChatSerializer


class CommunicationAPIView(APIView):

    def get(self, request, *args, pk=None, **kwargs):
        case = get_object_or_404(Case, pk=pk)
        parties = list(case.external_parties.values_list('id', flat=True))
        parties.append(case.customer.pk)
        chats = request.user.worker_chats.filter(type=Chat.Type.whats_app, party__id__in=parties)
        serializer = ChatSerializer(chats, many=True, context={'request': request, 'case': case})
        return Response(serializer.data)
