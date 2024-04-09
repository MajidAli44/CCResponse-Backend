from datetime import date
from core.models import Invoice


class TemplateField:

    def __init__(self, case):
        self.case = case
        self.storage_invoices = self.case.invoices.filter(
            invoice_type=Invoice.InvoiceType.storage_recovery,
            vehicle_storage__isnull=False
        )
        self.hire_invoices = self.case.invoices.filter(
            invoice_type=Invoice.InvoiceType.hire,
            vehicle_hire__isnull=False
        )
        self.recovery_invoices = self.case.invoices.filter(
            invoice_type=Invoice.InvoiceType.storage_recovery,
            vehicle_recovery__isnull=False
        )

    @staticmethod
    def todays_date():
        return date.today().strftime("%d/%m/%Y")

    def case_ref(self):
        return f'CC/{self.case.id}'

    def cdw(self):
        return self.hire_invoices[0].vehicle_hire.cwd_per_day if self.hire_invoices.exists() else 0

    def client_name(self):
        return self.case.customer.name

    def client_address(self):
        return self.case.customer.address

    def client_dob(self):
        return self.case.customer.date_of_birth.strftime("%d/%m/%Y") if self.case.customer.date_of_birth else ""

    def client_vehicle_make_and_model(self):
        return f'{self.case.customer_vehicle.make} {self.case.customer_vehicle.model}'

    def client_reg(self):
        return self.case.customer_vehicle.vrn

    def third_party_reg(self):
        return self.case.third_party.vehicle.vrn

    def third_party_name(self):
        return self.case.third_party.name

    def hire_vehicle_reg(self):
        return self.hire_invoices[0].vehicle_hire.vehicle.vrn if self.hire_invoices.exists() else ""

    def hire_vehicle_make_and_model(self):
        if self.hire_invoices.exists():
            hire_vehicle = self.hire_invoices[0].vehicle_hire.vehicle
            return f'{hire_vehicle.make} {hire_vehicle.model}'
        return ""

    def hire_daily_rate(self):
        return self.hire_invoices[0].vehicle_hire.daily_hire_rate if self.hire_invoices.exists() else 0

    def hire_total_max_daily_rate(self):
        return self.hire_daily_rate() + self.cdw()

    def number_of_days_hired(self):
        return (self.hire_invoices[0].vehicle_hire.end_date - self.hire_invoices[0].vehicle_hire.start_date).days + 1 \
            if self.hire_invoices.exists() \
               and self.hire_invoices[0].vehicle_hire.start_date\
               and self.hire_invoices[0].vehicle_hire.end_date \
            else 0

    def hire_start_date(self):
        return self.hire_invoices[0].vehicle_hire.start_date.strftime("%d/%m/%Y") if self.hire_invoices.exists() else ""

    def hire_end_date(self):
        return self.hire_invoices[0].vehicle_hire.end_date.strftime("%d/%m/%Y") \
            if self.hire_invoices.exists() and self.hire_invoices[0].vehicle_hire.end_date \
            else ""

    def days_in_storage(self):
        return (self.storage_invoices[0].vehicle_storage.end_date - self.storage_invoices[
            0].vehicle_storage.start_date).days + 1 \
            if self.storage_invoices.exists() \
               and self.storage_invoices[0].vehicle_storage.start_date \
               and self.storage_invoices[0].vehicle_storage.end_date \
            else 0

    def storage_start_date(self):
        return self.storage_invoices[0].vehicle_storage.start_date.strftime("%d/%m/%Y") \
            if self.storage_invoices.exists() \
            else ""

    def storage_end_date(self):
        return self.storage_invoices[0].vehicle_storage.end_date.strftime("%d/%m/%Y") \
            if self.storage_invoices.exists() and self.storage_invoices[0].vehicle_storage.end_date \
            else ""

    def recovery_net_amount(self):
        return sum([invoice.vehicle_recovery.total_price for invoice in self.recovery_invoices])

    def engineers_fee(self):
        return self.recovery_invoices[0].vehicle_recovery.engineers_fee or 0 if self.recovery_invoices.exists() else 0

    def date_of_accident(self):
        return self.case.date_of_accident.strftime("%d/%m/%Y")

    def date_engineer_instructed(self):
        if self.hire_invoices.exists():
            hire_validation = getattr(self.hire_invoices[0].vehicle_hire, "hire_validation", None)
            date_engineer_instructed = hire_validation and hire_validation.engs_instructed_date
            if date_engineer_instructed:
                return date_engineer_instructed.strftime("%d/%m/%Y")
        return ""

    def date_of_inspection(self):
        if self.hire_invoices.exists():
            hire_validation = getattr(self.hire_invoices[0].vehicle_hire, "hire_validation", None)
            inspection_date = hire_validation and hire_validation.inspection_date
            if inspection_date:
                return inspection_date.strftime("%d/%m/%Y")
        return ""

    def date_report_received(self):
        if self.hire_invoices.exists():
            hire_validation = getattr(self.hire_invoices[0].vehicle_hire, "hire_validation", None)
            date_report_received = hire_validation and hire_validation.report_received_date
            if date_report_received:
                return date_report_received.strftime("%d/%m/%Y")
        return ""

    def date_fnol_sent_to_tp(self):
        if self.hire_invoices.exists():
            hire_validation = getattr(self.hire_invoices[0].vehicle_hire, "hire_validation", None)
            send_to_tp_date = hire_validation and hire_validation.send_to_tp_date
            if send_to_tp_date:
                return send_to_tp_date.strftime("%d/%m/%Y")
        return ""

    def date_repair_authorised(self):
        if self.recovery_invoices.exists():
            date_repair_authorised = self.recovery_invoices[0].vehicle_recovery.date_repair_authorized
            if date_repair_authorised:
                return date_repair_authorised.strftime("%d/%m/%Y")
        return ""

    def date_satisfaction_note_signed(self):
        if self.recovery_invoices.exists():
            date_satisfaction_note_signed = self.recovery_invoices[0].vehicle_recovery.date_satisfaction_note_signed
            if date_satisfaction_note_signed:
                return date_satisfaction_note_signed.strftime("%d/%m/%Y")
        return ""


def get_template_context(case):
    template_field = TemplateField(case)
    return {
        'todays_date': template_field.todays_date(),
        'case_ref': template_field.case_ref(),
        'client_name': template_field.client_name(),
        'third_party_reg': template_field.third_party_reg(),
        'third_party_name': template_field.third_party_name(),
        'date_of_accident': template_field.date_of_accident(),
        'client_address': template_field.client_address(),
        'client_dob': template_field.client_dob(),
        'client_vehicle_make_and_model': template_field.client_vehicle_make_and_model(),
        'client_reg': template_field.client_reg(),
        'storage_start_date': template_field.storage_start_date(),
        'hire_vehicle_reg': template_field.hire_vehicle_reg(),
        'hire_vehicle_make_and_model': template_field.hire_vehicle_make_and_model(),
        'hire_daily_rate': template_field.hire_daily_rate(),
        'cdw': template_field.cdw(),
        'hire_total_max_daily_rate': template_field.hire_total_max_daily_rate(),
        'hire_total_max_daily_rate_CR': float(template_field.hire_total_max_daily_rate()) * 1.3,
        'hire_start_date': template_field.hire_start_date(),
        'hire_end_date': template_field.hire_end_date(),
        'number_of_days_hired': template_field.number_of_days_hired(),
        'recovery_net_amount': template_field.recovery_net_amount(),
        'engineers_fee': template_field.engineers_fee(),
        'days_in_storage': template_field.days_in_storage(),
        'storage_end_date': template_field.storage_end_date(),
        'date_engineer_instructed': template_field.date_engineer_instructed(),
        'date_of_inspection': template_field.date_of_inspection(),
        'date_report_received': template_field.date_report_received(),
        'date_fnol_sent_to_tp': template_field.date_fnol_sent_to_tp(),
        'date_repair_authorised': template_field.date_repair_authorised(),
        'date_satisfaction_note_signed': template_field.date_satisfaction_note_signed()
    }
