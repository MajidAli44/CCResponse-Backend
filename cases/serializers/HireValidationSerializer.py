from rest_framework import serializers

from cases.models import HireValidation


class HireValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HireValidation
        fields = (
            'engs_instructed', 'report_received', 'sent_to_tp',
            'inspection_date', 'repairable', 'total_loss_cil',
            'repair_auth', 'sat_note_sign', 'settle_offer',
            'offer_accepted', 'cheque_received', 'liability_admitted', 'liability_admitted_date',
        )
