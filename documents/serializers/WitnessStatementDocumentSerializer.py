from rest_framework import serializers

from cases.models import Case


class WitnessStatementDocumentSerializer(serializers.ModelSerializer):
    # The witness statement document has no fields to fill in

    class Meta:
        model = Case
        fields = ()
