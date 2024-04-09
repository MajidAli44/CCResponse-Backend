from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Case, ExternalParty, Injury

from core.serializers import IntroducerSerializer, SolicitorSerializer, ThirdPartyInsurerSerializer, ExternalPartyInsurerSerializer


class CaseCreationDataAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = {
            "external_parties": {
                "roles": [ExternalParty.Role.insurer, ExternalParty.Role.solicitor, ExternalParty.Role.introducer],
                'insurers': ExternalPartyInsurerSerializer(
                    instance=ExternalParty.objects.filter(role=ExternalParty.Role.insurer, is_third_party=False),
                    many=True).data,
                'introducers': IntroducerSerializer(
                    instance=ExternalParty.objects.filter(role=ExternalParty.Role.introducer, is_third_party=False),
                    many=True).data,
                'solicitors': SolicitorSerializer(
                    instance=ExternalParty.objects.filter(role=ExternalParty.Role.solicitor, is_third_party=False),
                    many=True).data
            },
            "case": {
                "status": dict(Case.Status.choices),
                "circumstances": dict(Case.Circumstances.choices),
                "payment_status": dict(Case.PaymentStatus.choices)
            },
            "third_party": {
                "insurers":
                    ThirdPartyInsurerSerializer(
                        instance=ExternalParty.objects.filter(role=ExternalParty.Role.insurer, is_third_party=True),
                        many=True).data
            },
            "injuries": {
                "statuses": Injury.Status.choices,
                "types": Injury.Type.choices
            }
        }
        return Response(data)
