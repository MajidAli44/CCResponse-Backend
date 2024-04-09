from datetime import datetime
from decimal import Decimal
from io import BytesIO

from docxtpl import DocxTemplate

from documents.generators import AbstractDocumentGenerator
from documents.serializers import RepairInvoiceDocumentSerializer
from invoices.models import InvoiceFile


class RepairInvoiceDocumentGenerator(AbstractDocumentGenerator):

    def document_name(self):
        return 'Repair Invoice.docx'

    def fields(self):
        return [
            'current_date', 'client_cc_ref', 'client_name', 'accident_date', 'tp_name', 'tp_insurer_ref', 'client_vrn'
        ]

    def document_serializer(self):
        return RepairInvoiceDocumentSerializer

    def is_docx_template(self):
        return True

    def is_pdf_file(self):
        return False

    def get_services_and_prices(self):
        case = self.get_case()
        if case.repair_invoice is None:
            return Decimal('0.00'), Decimal('0.00'), Decimal('0.00'), {}

        repair_invoice = case.repair_invoice

        services_and_prices = []

        if repair_invoice.labour_rate is not None and repair_invoice.labour_hours is not None:
            services_and_prices.append(
                {
                    'name': f'Labour: {Decimal(repair_invoice.labour_hours).quantize(Decimal("0.00"))}hrs @ £{Decimal(repair_invoice.labour_rate).quantize(Decimal("0.00"))} ph',
                    'price': (Decimal(repair_invoice.labour_hours) * Decimal(repair_invoice.labour_rate)).quantize(Decimal('0.00'))
                }
            )

        if repair_invoice.paint_and_sundries is not None:
            services_and_prices.append({'name': 'Paint and Sundries', 'price': repair_invoice.paint_and_sundries})

        if repair_invoice.parts_mlp is not None:
            services_and_prices.append({'name': 'Parts @ MLP', 'price': repair_invoice.parts_mlp})

        if repair_invoice.remove_and_refit_glass is not None:
            services_and_prices.append({'name': 'Remove and Refit Glass', 'price': repair_invoice.remove_and_refit_glass})

        if repair_invoice.covid_clean_and_ppe is not None:
            services_and_prices.append({'name': 'COVID-19 Clean + PPE', 'price': repair_invoice.covid_clean_and_ppe})

        if repair_invoice.specialist_1 is not None:
            services_and_prices.append({'name': 'Specialist 1', 'price': repair_invoice.specialist_1})

        if repair_invoice.miscellaneous_1 is not None:
            services_and_prices.append({'name': 'Miscellaneous 1', 'price': repair_invoice.miscellaneous_1})

        if repair_invoice.car_kit_and_mini_valet is not None:
            services_and_prices.append({'name': 'Car Car Kit and Mini Valet', 'price': repair_invoice.car_kit_and_mini_valet})

        if repair_invoice.geometry is not None:
            services_and_prices.append({'name': 'Geometry', 'price': repair_invoice.geometry})

        if repair_invoice.anti_corrosion is not None:
            services_and_prices.append({'name': 'Anti Corrosion', 'price': repair_invoice.anti_corrosion})

        if repair_invoice.epa is not None:
            services_and_prices.append({'name': 'EPA', 'price': repair_invoice.epa})

        for item in repair_invoice.items.values():
            services_and_prices.append({'name': item['name'], 'price': item['price']})

        services_list = {}
        total_net = Decimal('0.00')
        total_vat = Decimal('0.00')
        current_service_number = 1
        for current_service in services_and_prices:
            total_net += current_service['price']
            vat = Decimal(current_service['price'] * Decimal(0.2)).quantize(Decimal('0.00'))
            total_vat += vat

            services_list[f'line{current_service_number}'] = current_service['name']
            services_list[f'line{current_service_number}_price'] = f'£{self.prepare_value(Decimal(current_service["price"]))}'
            services_list[f'line{current_service_number}_vat'] = f'£{self.prepare_value(Decimal(vat))}'

            current_service_number += 1

        total_net = total_net.quantize(Decimal('0.00'))
        total_vat = total_vat.quantize(Decimal('0.00'))
        total = (total_net + total_vat).quantize(Decimal('0.00'))

        return total_net, total_vat, total, services_list

    def process_fields_before_render(self, fields: dict):

        # Mark repair invoice
        invoice = InvoiceFile.objects.get_or_create(case=self.get_case())
        invoice = invoice[0]

        if 'total' in fields:
            invoice.recovery_invoice_date = datetime.today()
            invoice.recovery_invoice_total = fields['storage_total']

        invoice.last_invoice_date = datetime.today()
        invoice.save()

        return fields

    def generate_docx_template(self):
        total_net, total_vat, total, services_list = self.get_services_and_prices()

        template_path = self.get_template_path()
        filled_fields = self.document_serializer()(self.get_case()).data

        not_filled_fields = []
        template_data = {}

        for key in self.fields():
            if key not in filled_fields:
                not_filled_fields.append(key)

        for key, value in filled_fields.items():
            if value is None and key in self.fields():
                if key not in not_filled_fields:
                    not_filled_fields.append(key)
                template_data[key] = ''
                continue
            template_data[key] = AbstractDocumentGenerator.prepare_value(value)

        template_data.update(services_list)
        template_data['total_net'] = self.prepare_value(total_net.quantize(Decimal('0.00')))
        template_data['total_vat'] = self.prepare_value(total_vat.quantize(Decimal('0.00')))
        template_data['total'] = self.prepare_value(total.quantize(Decimal('0.00')))

        template = DocxTemplate(template_path)
        template.render(template_data)

        file_bytes = BytesIO()
        template.save(file_bytes)
        file_bytes.seek(0)

        return not_filled_fields, file_bytes