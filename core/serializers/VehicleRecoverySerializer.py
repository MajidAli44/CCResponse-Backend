
from core.models import VehicleRecovery
from .VehicleActionSerializer import VehicleActionSerializer


class VehicleRecoverySerializer(VehicleActionSerializer):
    class Meta:
        model = VehicleRecovery
        fields = '__all__'
