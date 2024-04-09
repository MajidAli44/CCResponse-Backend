from django.db import models


class VehicleHireValidation(models.Model):
    vehicle_hire = models.OneToOneField('VehicleHire', on_delete=models.CASCADE, related_name='hire_validation')

    engs_instructed_date = models.DateField(null=True, blank=True)
    inspection_date = models.DateField(null=True, blank=True)
    report_received_date = models.DateField(null=True, blank=True)
    send_to_tp_date = models.DateField(null=True, blank=True)
    repairable = models.BooleanField(default=True)
    total_loss_cil = models.BooleanField(default=True)
    settle_offer = models.BooleanField(default=False)
    offer_accepted = models.BooleanField(default=False)
    cheque_received = models.BooleanField(default=False)
    liability_admitted = models.BooleanField(default=False)
