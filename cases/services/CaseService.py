from decimal import Decimal

from django.db.models import Case as Db_Case, Count, F
from django.db.models import Sum, IntegerField, When
from django.db.models.functions import Coalesce

from cases.models import UserDisplayCaseColumn, Case, RecoveryDetail, CaseFieldsDefaultPrice


class CaseService:
    _model = Case

    @staticmethod
    def get_user_display_columns(user):
        if UserDisplayCaseColumn.objects.filter(user=user).exists():
            return UserDisplayCaseColumn.objects.get(user=user)

        return UserDisplayCaseColumn.objects.create(
            user=user,
            columns=[
                UserDisplayCaseColumn.CaseColumns.instruction_date, UserDisplayCaseColumn.CaseColumns.cc_ref,
                UserDisplayCaseColumn.CaseColumns.client_name, UserDisplayCaseColumn.CaseColumns.phone_number,
                UserDisplayCaseColumn.CaseColumns.status, UserDisplayCaseColumn.CaseColumns.provider,
                UserDisplayCaseColumn.CaseColumns.notes
            ]
        )

    @classmethod
    def get_each_status_count_of_cases(cls):
        return cls._model.objects.all().aggregate(
            all_count=Count(F('id')),
            lead_count=Coalesce(Sum(Db_Case(
                When(status=Case.CaseStatuses.lead, then=1),
                output_field=IntegerField())
            ), 0),
            ongoing_count=Coalesce(Sum(Db_Case(
                When(status=Case.CaseStatuses.ongoing, then=1),
                output_field=IntegerField())
            ), 0),
            payment_pack_count=Coalesce(Sum(Db_Case(
                When(status=Case.CaseStatuses.payment_pack, then=1),
                output_field=IntegerField())
            ), 0),
            settled_count=Coalesce(Sum(Db_Case(
                When(status=Case.CaseStatuses.settled, then=1),
                output_field=IntegerField())
            ), 0),
            closed_count=Coalesce(Sum(Db_Case(
                When(status=Case.CaseStatuses.closed, then=1),
                output_field=IntegerField())
            ), 0),
        )

    @staticmethod
    def calculate_hire_total_net(case: Case):
        total_net = Decimal('0.00')
        hire_detail = case.hire_detail
        if hire_detail and hire_detail.start_date:
            days_in_hire = hire_detail.days_in_hire

            total_net += ((hire_detail.collection or 0) + (hire_detail.delivery or 0))
            total_net_fields = [
                hire_detail.sat_nav, hire_detail.auto,
                hire_detail.towbar, hire_detail.bluetooth, (hire_detail.ns_driver_fee or 0)
            ]
            for total_net_field in total_net_fields:
                total_net += (total_net_field or 0) * days_in_hire
            total_net += ((hire_detail.driver_fee or 0) if hire_detail.driver_required else 0) * days_in_hire
            total_net += ((hire_detail.charge or 0) * days_in_hire)
            total_net += (hire_detail.cdw or 0) * days_in_hire if hire_detail.cdw_required else 0
            total_net += Decimal('45.0') if days_in_hire > 0 else Decimal('0.00')
        return total_net

    @staticmethod
    def winching_time_prices(winching_time):
        default_prices = CaseFieldsDefaultPrice.objects.last()
        if not default_prices:
            return {
                RecoveryDetail.WinchingTimes.minutes_30: Decimal('45.00'),
                RecoveryDetail.WinchingTimes.hour_1: Decimal('90.00'),
            }.get(winching_time, 0)
        return {
            RecoveryDetail.WinchingTimes.minutes_30: default_prices.recovery_detail_minutes_30 or Decimal('45.00'),
            RecoveryDetail.WinchingTimes.hour_1: default_prices.recovery_detail_hour_1 or Decimal('90.00'),
        }.get(winching_time, 0)

    @classmethod
    def calculate_storage_total_net(cls, case: Case):

        default_prices = CaseFieldsDefaultPrice.objects.first()

        total_net = Decimal('0.00')
        storage_detail = case.storage_detail
        recovery_detail = case.recovery_detail
        if storage_detail and storage_detail.from_date:
            days_in_storage = storage_detail.days_in_storage
            total_net += (storage_detail.fee_per_day or 0) * days_in_storage
        total_net += storage_detail.engineers_fee or 0
        if recovery_detail:
            total_net += (
                    (recovery_detail.call_out_charge or 0) +
                    (recovery_detail.inherited_fees or 0) +
                    cls.winching_time_prices(recovery_detail.winching_time)
            )
            if default_prices:
                if recovery_detail.road_cleanup:
                    total_net += default_prices.recovery_detail_road_cleanup
                if recovery_detail.skates == RecoveryDetail.Skates.one:
                    total_net += default_prices.hire_detail_one_fee_for_skates
                elif recovery_detail.skates == RecoveryDetail.Skates.two:
                    total_net += default_prices.hire_detail_one_fee_for_skates * 2
                elif recovery_detail.skates == RecoveryDetail.Skates.three:
                    total_net += default_prices.hire_detail_one_fee_for_skates * 3
                elif recovery_detail.skates == RecoveryDetail.Skates.four:
                    total_net += default_prices.hire_detail_one_fee_for_skates * 4
                elif recovery_detail.skates == RecoveryDetail.Skates.five:
                    total_net += default_prices.hire_detail_one_fee_for_skates * 5

        return total_net
