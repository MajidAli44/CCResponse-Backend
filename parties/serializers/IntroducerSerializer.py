from rest_framework import serializers

from parties.models import Introducer


class IntroducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introducer
        fields = ('id', 'name', 'company_number', 'contact_number', 'office_number', 'pi_fee', 'hire_fee', 'address')
