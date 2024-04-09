from rest_framework import serializers

from cases.services import CaseService
case_service = CaseService()


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)
        user_allowed_columns = set(
            case_service
                .get_user_display_columns(self.context['request'].user).columns
        )
        user_allowed_columns.add('id')

        for field_name in set(self.fields.keys()) - set(user_allowed_columns):
            self.fields.pop(field_name)
