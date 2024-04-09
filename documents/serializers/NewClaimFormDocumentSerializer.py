from rest_framework import serializers

from cases.models import Case


class NewClaimFormDocumentSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name', allow_null=True)
    client_phone_number = serializers.CharField(source='client.phone_number', allow_null=True)
    client_email_address = serializers.CharField(source='client.email', allow_null=True)
    client_date_of_birth = serializers.DateField(source='client.date_of_birth', allow_null=True)
    client_address = serializers.CharField(source='client.address', allow_null=True)
    client_postcode = serializers.CharField(source='client.postcode', allow_null=True)
    client_vrn = serializers.CharField(source='client.vehicle.vrn', allow_null=True)
    client_vehicle_make = serializers.CharField(source='client.vehicle.make', allow_null=True)
    client_vehicle_model = serializers.CharField(source='client.vehicle.model', allow_null=True)
    client_mot_expiry = serializers.DateField(source='client.vehicle.mot_expiry', allow_null=True)
    client_tax_expiry = serializers.DateField(source='client.vehicle.tax_expiry', allow_null=True)
    client_insurer_name = serializers.CharField(source='client.insurer.name', allow_null=True)
    client_ni_number = serializers.CharField(source='client.ni_number', allow_null=True)
    client_d_licence = serializers.CharField(source='client.license_number', allow_null=True)
    client_extra = serializers.CharField(source='accident.other_info', allow_null=True)

    accident_date = serializers.DateField(source='accident.accident_date', allow_null=True)
    approx_time = serializers.CharField(source='accident.approx_time', allow_null=True)
    approx_location = serializers.CharField(source='accident.location', allow_null=True)
    approx_circumstances = serializers.CharField(source='accident.circumstances', allow_null=True)
    approx_other_info = serializers.CharField(source='client.notes', allow_null=True)

    tp_name = serializers.CharField(source='third_party.name', allow_null=True)
    tp_address = serializers.CharField(source='third_party.address', allow_null=True)
    tp_phone_number = serializers.CharField(source='third_party.phone_number')
    tp_vrn = serializers.CharField(source='third_party.vehicle.vrn', allow_null=True)
    tp_vehicle_make = serializers.CharField(source='third_party.vehicle.make', allow_null=True)
    tp_vehicle_model = serializers.CharField(source='third_party.vehicle.model', allow_null=True)
    tp_mot_expiry = serializers.DateField(source='third_party.vehicle.mot_expiry', allow_null=True)
    tp_tax_expiry = serializers.DateField(source='third_party.vehicle.tax_expiry', allow_null=True)
    tp_insurer = serializers.CharField(source='third_party.insurer.name', allow_null=True)
    tp_policy_number = serializers.CharField(source='third_party.policy_number', allow_null=True)
    tp_insurer_phone_number = serializers.CharField(source='third_party.insurer_contact_number', allow_null=True)
    tp_insurer_email = serializers.CharField(source='third_party.insurer_email', allow_null=True)
    tp_insurer_ref = serializers.CharField(source='third_party.insurer_ref', allow_null=True)
    tp_other_details = serializers.CharField(source='third_party.other_details', allow_null=True)

    # Concatenate client_address and client_postcode
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['client_address'] is not None and representation['client_postcode'] is not None:
            representation['client_address'] += '\n' + representation['client_postcode']
        return representation

    class Meta:
        model = Case
        fields = (
            'client_name', 'client_phone_number', 'client_email_address', 'client_date_of_birth', 'client_address',
            'client_vrn', 'client_vehicle_model', 'client_vehicle_make', 'accident_date', 'approx_location',
            'approx_circumstances', 'approx_other_info', 'tp_name', 'tp_address', 'tp_vrn', 'tp_vehicle_make',
            'tp_vehicle_model', 'client_mot_expiry', 'client_tax_expiry', 'client_insurer_name', 'approx_time',
            'tp_mot_expiry', 'tp_tax_expiry', 'tp_insurer', 'tp_policy_number', 'tp_insurer_phone_number',
            'tp_insurer_email', 'tp_insurer_ref', 'tp_other_details', 'client_ni_number', 'client_extra',
            'client_d_licence', 'tp_phone_number', 'client_postcode'
        )
