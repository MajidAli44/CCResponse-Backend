from rest_framework import serializers

from parties.models import Solicitor


class SolicitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitor
        fields = ('id', 'name', 'fullname', 'hotkey_number', 'contact_number', 'pi_fee', 'address', 'notes')
