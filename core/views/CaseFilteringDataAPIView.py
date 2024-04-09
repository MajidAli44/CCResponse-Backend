from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Case, ExternalParty, Customer


class CaseFilteringDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'case': {
                'status': [i for i in Case.Status.values]
            },
            'customers': Customer.objects.values('id', 'name', 'phone_number'),
            'external_parties': {
                'introducers': ExternalParty.objects.filter(role=ExternalParty.Role.introducer,
                                                            is_third_party=False).values('id', 'name'),
                'solicitors': ExternalParty.objects.filter(role=ExternalParty.Role.solicitor,
                                                           is_third_party=False).values('id', 'name')
            }
        })
