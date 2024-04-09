from rest_framework import serializers

from cases.models import RecoveryDetail


class RecoveryDetailSerializer(serializers.ModelSerializer):
    total_recovery_fee = serializers.FloatField(source='recovery_fee', allow_null=True, read_only=True, default=0)

    class Meta:
        model = RecoveryDetail
        fields = (
            'recovery_date', 'recovery_type', 'other_recovery_reason',
            'call_out_charge', 'winching_time', 'road_cleanup', 'inherited_fees',
            'skates', 'total_recovery_fee'
        )
