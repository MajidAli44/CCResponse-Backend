from rest_framework import serializers

from cases.models import HireAgreement


class HireAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = HireAgreement
        fields = (
            'offer_received', 'personally_liable', 'vehicle_unroadworthy', 'no_another_vehicle',
            'prosecution', 'accident_loss_in_3_past_years', 'proposal_declined_or_increased_fees', 'diseases'
        )
