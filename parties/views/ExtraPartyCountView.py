from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from parties.models import Introducer, Solicitor, Insurer, Provider
from parties.serializers import ExtraPartyCountSerializer


class ExtraPartyCountAPIView(GenericAPIView):
    """ View for get count of all extra parties """
    serializer_class = ExtraPartyCountSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data={
            'solicitor_count': Solicitor.objects.all().count(),
            'insurer_count': Insurer.objects.count(),
            'introducer_count': Introducer.objects.all().count(),
            'provider_count': Provider.objects.all().count(),
        })
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.validated_data,
            status=status.HTTP_200_OK
        )
