from datetime import datetime
from decimal import Decimal

from documents.generators import AbstractDocumentGenerator
from documents.serializers import PaymentPackDocumentSerializer
from invoices.models import InvoiceFile


class PaymentPackDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'Payment Pack.docx'

    def fields(self):
        return [
            'current_date', 'client_cc_ref', 'client_name', 'client_vrn', 'accident_date', 'tp_name', 'tp_vrn',
            'tp_insurer_ref', 'date_eng_instructed', 'date_inspection', 'date_report_received', 'date_sent_to_tp',
            'date_repair_authorized', 'date_settlement_offer', 'date_offer_accepted', 'date_cheque_received',
            'date_satisfaction_signed', 'storage_from', 'storage_to', 'storage_fee_per_day', 'days_in_storage',
            'recovery_call_out_charge', 'recovery_call_out_charge_vat', 'engineer_fee', 'engineer_fee_vat',
            'winching_time', 'winching_time_vat', 'road_cleanup', 'road_cleanup_vat', 'skates_total_sum',
            'skates_total_sum_vat', 'inherited_fees', 'inherited_fees_vat', 'storage_total_sum',
            'storage_total_sum_vat', 'storage_total_net', 'storage_total_vat', 'storage_total', 'storage_total_lt15',
            'storage_total_gt15', 'storage_total_gt30', 'hire_vehicle_make', 'hire_vehicle_model', 'hire_vrn',
            'hire_start_date', 'hire_end_date', 'hire_charge_per_day', 'days_in_hire', 'hire_total_sum',
            'hire_total_sum_vat', 'delivery_charge', 'delivery_charge_vat', 'collection_charge',
            'collection_charge_vat', 'cdw_per_day', 'additional_driver', 'sat_nav', 'auto', 'towbar', 'bluetooth',
            'ns_driver_surcharge', 'extras_total', 'extras_total_vat', 'hire_total_net', 'hire_total_vat',
            'hire_total', 'hire_total_lt15', 'hire_total_gt15', 'hire_total_gt30', 'abi_admin_fee', 'abi_admin_fee_vat',
            'winching_time_type', 'pay_pack_total_net', 'pay_pack_vat', 'pay_pack_total', 'pay_pack_vat_lt15',
            'pay_pack_total_lt15', 'pay_pack_vat_gt15', 'pay_pack_total_gt15', 'pay_pack_vat_gt30',
            'pay_pack_total_gt30', 'recovery_type'
        ]

    def document_serializer(self):
        return PaymentPackDocumentSerializer

    def is_docx_template(self):
        return True

    def is_pdf_file(self):
        return False

    def process_fields_before_render(self, fields: dict):

        # Mark hire and storage invoices
        invoice = InvoiceFile.objects.get_or_create(case=self.get_case())
        invoice = invoice[0]

        if 'hire_total' in fields:
            invoice.hire_invoice_date = datetime.today()
            invoice.hire_invoice_total = Decimal(str(fields['hire_total']).replace(',', ''))

        if 'storage_total' in fields:
            invoice.storage_invoice_date = datetime.today()
            invoice.storage_invoice_total = Decimal(str(fields['storage_total']).replace(',', ''))

        invoice.last_invoice_date = datetime.today()
        invoice.save()

        return fields
