from decimal import Decimal

from django.db import models


class CaseFieldsDefaultPrice(models.Model):
    """ Model for set case default prices """
    recovery_detail_minutes_30 = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(45.0))
    recovery_detail_hour_1 = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(90.0))
    recovery_detail_call_out_charge = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    recovery_detail_road_cleanup = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(50))
    recovery_detail_inherited_fees = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))

    storage_detail_fee_per_day = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    storage_detail_engineers_fee = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(125.0))

    hire_detail_collection = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(50.0))
    hire_detail_delivery = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(50.0))
    hire_detail_cdw = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    hire_detail_add_driver = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    hire_detail_sat_nav = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(5.0))
    hire_detail_auto = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(5.0))
    hire_detail_towbar = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(5.0))
    hire_detail_bluetooth = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(5.0))
    hire_detail_ns_drive_charge = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    hire_detail_rep_inv_amt = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    hire_detail_rep_inv_vat = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    hire_detail_rep_cost_outlay = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    hire_detail_hire_fee = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    hire_detail_recovery_fee = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    hire_detail_engineers_fee = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    hire_detail_storage_fee = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    hire_detail_one_fee_for_skates = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(25.0))

    repair_invoice_paint_and_sundries = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    repair_invoice_parts_mlp = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    repair_invoice_remove_and_refit_glass = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    repair_invoice_covid_clean_and_ppe = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    repair_invoice_specialist_1 = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    repair_invoice_miscellaneous_1 = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    repair_invoice_car_kit_and_mini_valet = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    repair_invoice_geometry = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    repair_invoice_anti_corrosion = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))
    repair_invoice_epa = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal(0.0))

    class Meta:
        verbose_name = 'Case fields default price'
