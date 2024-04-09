from decimal import Decimal

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from cases.models import PIDetail
from parties.serializers.PiClientSerializer import PiClientSerializer


class PIDetailSerializer(WritableNestedModelSerializer):
    pi_clients = PiClientSerializer(required=False, many=True, source='piclient_set')
    pi_total_fee = serializers.SerializerMethodField(read_only=True, allow_null=True, default=0)

    class Meta:
        model = PIDetail
        fields = (
            'claim_type', 'claim_num', 'solicitor_introduced',
            'instructed_paid_date', 'status', 'notes', 'provider', 'pi_status', 'pi_clients', 'pi_total_fee'
        )

    def get_pi_total_fee(self, obj):
        total = Decimal('0.0')
        for client in obj.piclient_set.all():
            total += Decimal(client.fee or '0.0') or Decimal('0.0')
        return total

