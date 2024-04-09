from rest_framework import serializers

from cases.models import Case


class StatementOfTruthDocumentSerializer(serializers.ModelSerializer):
    # The statement of truth document has no fields to fill in

    class Meta:
        model = Case
        fields = ()
