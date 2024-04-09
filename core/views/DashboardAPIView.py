from datetime import date

from django.db.models import Q, Sum

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cases.models import Case, HireDetail
from vehicles.models import HireVehicle
from core.models import Injury,  Invoice

class DashboardAPIView(APIView):

    def get(self, request):
        today = date.today()
        pp_stage_count = 0
        pp_stage = Case.objects.filter(
            Q(status_description='payment_pack_pp_issued') | Q(status_description='payment_pack_passed_to_ra'))

        if pp_stage.exists():
            for case in pp_stage:
                pp_stage_count += case.case_value

        due_in_count = 0
        due_in = Case.objects.filter(
            status_description='payment_pack_settlement_agreed')

        if due_in.exists():
            for case in due_in:
                due_in_count += case.case_value

        litigated_count = 0
        litigated = Case.objects.filter(
            status_description='payment_pack_passed_to_ra')

        if litigated.exists():
            for case in litigated:
                litigated_count += case.case_value

        # on hire
        vehicles_on_hire_ids = set(
            HireDetail.objects.filter(
                Q(end_date__isnull=True) | Q(end_date__gt=today),
                start_date__lte=today,
                vehicle_id__isnull=False, case__isnull=False
            ).values_list('vehicle_id', flat=True)
        )

        ongoing_files = Case.objects.filter(
            Q(status_description='lead_new_lead') |
            Q(status_description='ongoing_accepted') |
            Q(status_description='ongoing_in_hire') |
            Q(status_description='lead_awaiting_further_info') |
            Q(status_description='lead_hk_to_provider')
        ).count()

        number_of_vehicles = HireVehicle.objects.all().count()

        daily_incurring_count = 0
        daily_incurring = Case.objects.filter(status_description='ongoing_in_hire')

        if daily_incurring.exists():
            for case in daily_incurring:
                daily_incurring_count += (case.hire_detail.charge or 0)
                daily_incurring_count += (case.storage_detail.fee_per_day or 0)

        # Outstanding
        unsettled_invoices = Invoice.objects.filter(settlement_status=Invoice.SettlementStatus.unsettled)
        not_agreed_invoices = unsettled_invoices.filter(settled_amount_net=None, settled_amount_vat=None)
        agreed_invoices = unsettled_invoices.filter(settled_amount_net__isnull=False, settled_amount_vat__isnull=False)
        not_agreed_invoices_agg = not_agreed_invoices.aggregate(
            Sum('total_net'),
            Sum('total_vat')
            )
        not_agreed_invoices_amount = (not_agreed_invoices_agg['total_net__sum'] or 0) + (not_agreed_invoices_agg['total_vat__sum'] or 0)

        data = {
            'total_outstanding': not_agreed_invoices_amount,
            'total_pi': Injury.objects.count(),
            'total_pp_stage': pp_stage_count,
            'due_in': due_in_count,
            'total_litigated': litigated_count,
            'cars_on_hire': len(vehicles_on_hire_ids),
            'total_vehicles': number_of_vehicles,
            'ongoing': ongoing_files,
            'daily_incurring': daily_incurring_count,

        }
        return Response(data, status=status.HTTP_200_OK)

#
# class DashboardAPIView(APIView):
#     @staticmethod
#     def __get_scheduled_to_chase():
#         today = date.today()
#         scheduled_to_chase = []
#         stcs = ScheduledToChaseCase.objects.filter(
#             chase_date__lte=today
#         ).order_by('chase_date').values(
#             'case_id', 'chase_date',
#             'case__customer__name', 'case__date_of_accident', 'user_last_scheduled_id',
#             'case__worker__first_name', 'case__worker__last_name', 'case__worker__username'
#         )
#
#         case_id_to_user_last_scheduled_id = {
#             data['case_id']: data['user_last_scheduled_id']
#             for data in stcs
#         }
#
#         last_case_notes = {}
#         case_notes = CaseNote.objects.filter(
#             case_id__in=case_id_to_user_last_scheduled_id.keys(),
#         ).order_by(
#             'created_at'
#         ).values(
#             'case_id', 'worker_id', 'created_at', 'note'
#         )
#
#         for case_note_data in case_notes:
#             case_id = case_note_data['case_id']
#             if case_id_to_user_last_scheduled_id[case_id] != case_note_data['worker_id']:
#                 # We only search for notes created by case owner
#                 continue
#
#             another_note_already_added = case_id in last_case_notes
#             if (
#                     another_note_already_added and last_case_notes[case_id]['created_at'] < case_note_data['created_at']
#                     or not another_note_already_added
#             ):
#                 last_case_notes[case_id] = case_note_data
#
#         for stc_data in stcs:
#             case_id = stc_data['case_id']
#             last_note = last_case_notes.get(case_id, None)
#             worker_name = (
#                     f'{stc_data["case__worker__first_name"] or ""} {stc_data["case__worker__last_name"] or ""}'.strip()
#                     or stc_data['case__worker__username']
#             )
#
#             scheduled_to_chase.append(
#                 {
#                     'id': case_id,
#                     'customer_name': stc_data['case__customer__name'],
#                     'doa': stc_data['case__date_of_accident'],
#                     'follow_up_setter_name': worker_name,
#                     'is_overdue': stc_data['chase_date'] < today,
#                     'note': last_note and last_note['note']
#                 }
#             )
#         return scheduled_to_chase
#
#     def get(self, request, *args, **kwargs):
#         today = date.today()
#         cases = Case.objects.all()
#
#         unsettled_invoices = Invoice.objects.filter(settlement_status=Invoice.SettlementStatus.unsettled)
#         not_agreed_invoices = unsettled_invoices.filter(settled_amount_net=None, settled_amount_vat=None)
#         agreed_invoices = unsettled_invoices.filter(settled_amount_net__isnull=False, settled_amount_vat__isnull=False)
#
#         not_agreed_invoices_agg = not_agreed_invoices.aggregate(
#             Sum('total_net'),
#             Sum('total_vat')
#         )
#         not_agreed_invoices_amount = (
#                                              not_agreed_invoices_agg['total_net__sum'] or 0
#                                      ) + (
#                                              not_agreed_invoices_agg['total_vat__sum'] or 0
#                                      )
#         agreed_invoices_agg = agreed_invoices.aggregate(
#             Sum('settled_amount_net'),
#             Sum('total_net')
#         )
#
#         storage_incurring = VehicleStorage.objects.filter(
#             Q(end_date__isnull=True) | Q(end_date__gte=today),
#             start_date__lte=today
#         ).aggregate(
#             storage_incurring=Sum(
#                 F('daily_storage_rate') * (
#                         ExtractDay(
#                             F('end_date') - F('start_date')
#                         ) + 1
#                 ),
#                 output_field=DecimalField()
#             )
#         )['storage_incurring'] or 0
#
#         booking_incurring = VehicleHire.objects.filter(
#             Q(end_date__isnull=True) | Q(end_date__gte=today),
#             start_date__lte=today
#         ).aggregate(
#             booking_incurring=Sum(
#                 F('daily_hire_rate') * (
#                         ExtractDay(
#                             F('end_date') - F('start_date')
#                         ) + 1
#                 ),
#                 output_field=DecimalField()
#             )
#         )['booking_incurring'] or 0
#
#         vehicles_on_hire_ids = set(
#             VehicleHire.objects.filter(
#                 Q(end_date__isnull=True) | Q(end_date__gte=today),
#                 start_date__lte=today,
#                 vehicle__owner=Vehicle.Owner.company,
#             ).values_list('vehicle_id')
#         )
#
#         data = {
#             'general': {
#                 'total_due_in': (
#                         agreed_invoices_agg['total_net__sum'] - agreed_invoices_agg['settled_amount_net__sum']
#                 ),
#                 'total_outstanding': not_agreed_invoices_amount,
#                 'payment_pack_stage_amount': not_agreed_invoices_amount,
#                 'total_daily_incurring': storage_incurring + booking_incurring,
#                 'cars_on_hire': len(vehicles_on_hire_ids),
#                 'total_cars': Vehicle.objects.filter(owner=Vehicle.Owner.company).count(),
#                 'total_pi': Injury.objects.count(),
#                 'ongoing_files': cases.filter(status=Case.Status.ongoing).count(),
#                 'payment_pack_stage_count': cases.filter(status=Case.Status.payment_pack).count()
#             },
#             'scheduled_to_chase': self.__get_scheduled_to_chase(),
#             'comms_notifications': [
#                 {
#                     "id": None,
#                     "subject": None,
#                     "sender_name": None,
#                     "message": None,
#                     "attachments": [],
#                     "received_at": None,
#                     "chat_type": None,
#                     "ref": None
#                 }
#             ],
#             'diagram': {
#                 "company": None,
#                 "google": None,
#                 "introducer": None
#             }
#         }
#         return Response(data, status=status.HTTP_200_OK)
