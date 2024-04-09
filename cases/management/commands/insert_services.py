from django.core.management.base import BaseCommand

from cases.models import Case


class Command(BaseCommand):
    help = 'Sets default values for services'

    def handle(self, *args, **options):
        cases = Case.objects.all()
        for case in cases:
            service = ["cd"]
            if case.hire_detail is not None:
                if case.hire_detail.start_date or case.hire_detail.end_date:
                    service.append("hd")

            if case.storage_detail is not None:
                if case.storage_detail.from_date or case.storage_detail.end_date:
                    service.append("sr")

            if case.recovery_detail is not None:
                if case.recovery_detail.recovery_date or case.recovery_detail.call_out_charge or case.recovery_detail.winching_time:
                    if "sr" not in service:
                        service.append("sr")
                    else:
                        pass

            if case.pi_detail is not None:
                if case.pi_detail.instructed_paid_date:
                    service.append("pi")

            if case.hire_validation is not None:
                if case.hire_validation.engs_instructed or case.hire_validation.repairable:
                    service.append("vd")

            if case.case_fee is not None:
                if case.case_fee.repair_status or case.case_fee.salvage_value or case.case_fee.sale_price or case.case_fee.sold_via:
                    service.append("sv")
            case.services = service
            self.stdout.write(self.style.SUCCESS(f'Saving case no {case.id} => services array {service}'))
            case.save()
        # Case.objects.all().update(services=default_value)
        self.stdout.write(self.style.SUCCESS('Services values set successfully.'))
