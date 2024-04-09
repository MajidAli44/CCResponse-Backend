from drf_writable_nested import WritableNestedModelSerializer

from parties.models import ThirdParty
from vehicles.serializers import ThirdPartyVehicleSerializer


class ThirdPartySerializer(WritableNestedModelSerializer):
    vehicle = ThirdPartyVehicleSerializer(required=False, allow_null=True)

    class Meta:
        model = ThirdParty
        fields = (
            'id', 'name', 'phone_number', 'email', 'notes', 'address', 'postcode',
            'policy_number', 'other_details', 'insurer', 'vehicle',
            'insurer_email', 'insurer_contact_number', 'insurer_ref'
        )
