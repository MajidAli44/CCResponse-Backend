from collections import defaultdict

from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from core.models import Case, CaseNote, ExternalParty, ExternalPartyService, Customer, Injury
from core.serializers import CaseSerializer
from core.utils import PaginatedQSMixin


class CasesAPI(APIView, PaginatedQSMixin):
    search_fields = ['customer__name', 'title']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.case_fields = Case.__dict__.copy()
        self.case_fields.update(
            {'customer__name': Customer.name, 'customer__phone_number': Customer.phone_number}
        )

    def get(self, request, *args, **kwargs):
        qs = Case.objects.all().exclude(status=Case.Status.rejected)

        (
            truncated_qs, count, additional_counts,
            old_query_params, page, page_size, _
        ) = self.apply_query_params(
            request.query_params, qs, self.case_fields, self.search_fields, 'status',
            {'Ongoing': Case.Status.ongoing, 'Payment Pack': Case.Status.payment_pack, 'Settled': Case.Status.settled},
            additional_count_fields_to_exclude_from_filter_config=('pk', 'id')
        )
        data = self.build_paginated_response_without_results(request, old_query_params, count, page, page_size)

        cases_ids = truncated_qs.values_list('id', flat=True)

        id_to_introducers_arr = defaultdict(list)
        for case_id, ext_party_name in ExternalPartyService.objects.filter(
                external_party__role=ExternalParty.Role.introducer, external_party__is_third_party=False,
                case_id__in=cases_ids
        ).values_list('case_id', 'external_party__name'):
            id_to_introducers_arr[case_id].append(ext_party_name)

        id_to_solicitors_arr = defaultdict(list)
        for case_id, ext_party_name in ExternalPartyService.objects.filter(
                external_party__role=ExternalParty.Role.solicitor, external_party__is_third_party=False,
                case_id__in=cases_ids
        ).values_list('case_id', 'external_party__name'):
            id_to_solicitors_arr[case_id].append(ext_party_name)

        id_to_notes_data = defaultdict(list)
        for note_data in CaseNote.objects.filter(
                case_id__in=cases_ids
        ).values('case_id', 'note', 'worker__first_name', 'worker__last_name', 'worker__username', 'created_at'):
            id_to_notes_data[note_data['case_id']].append(
                {
                    'text': note_data['note'],
                    'owner': (
                        f'{note_data["worker__first_name"] or ""} {note_data["worker__last_name"] or ""}'.strip() if (
                                note_data["worker__last_name"] or note_data["worker__last_name"]
                        ) else note_data['worker__username']
                    ),
                    'created_at': note_data['created_at']
                }
            )

        id_to_injuries_data = defaultdict(list)
        for injury_data in Injury.objects.filter(
                case_id__in=cases_ids
        ).values('case_id', 'id', 'solicitor', 'date', 'status', 'type'):
            case_id = injury_data.pop('case_id')
            id_to_injuries_data[case_id].append(injury_data)

        data['additional_counts'] = additional_counts
        data['additional_counts_label_to_value'] = {
            label: value
            for value, label in Case.Status.choices
        }
        data['results'] = [
            {
                'id': case_data['id'],
                'created_at': case_data['created_at'].strftime(settings.DEFAULT_DATE_FORMAT),
                'date_of_accident': case_data['date_of_accident'].strftime(settings.DEFAULT_DATE_FORMAT),
                'status': case_data['status'],
                'customer': {
                    'name': case_data['customer__name'],
                    'phone_number': case_data['customer__phone_number'],
                },
                'external_parties': {
                    'introducers': id_to_introducers_arr.get(case_data['id'], []),
                    'solicitors': id_to_solicitors_arr.get(case_data['id'], []),
                },
                'injuries': id_to_injuries_data.get(case_data['id'], []),
                'case_notes': id_to_notes_data.get(case_data['id'], []),
                'tp_insurer_name': case_data['third_party__insurer__name']
            } for case_data in truncated_qs.values(
                'id',
                'customer__name', 'customer__phone_number',
                'created_at', 'date_of_accident', 'status',
                'third_party__insurer__name'
            )
        ]

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=CaseSerializer,
        responses={
            status.HTTP_201_CREATED: 'Created',
            status.HTTP_400_BAD_REQUEST: "Bad Request"
        },
        operation_id='cases_create',
    )
    def post(self, request, *args, **kwargs):
        serializer = CaseSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            obj = serializer.save()
            response = Response(status=status.HTTP_201_CREATED)
            response['Location'] = reverse('cases-detail', kwargs={'pk': obj.id})
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
