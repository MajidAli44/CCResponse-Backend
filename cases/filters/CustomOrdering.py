from rest_framework.filters import OrderingFilter


class CustomOrdering(OrderingFilter):
    """Custom ordering class for case list with field mapper"""

    def _field_mapper(self, field):
        fields = {
            'instruction_date': 'instruction_date',
            'accident_date': 'accident__accident_date',
            'client_name': 'client__name',
            'phone_number': 'client__phone_number',
            'introducer': 'introducer__name',
            'client_notes': 'client__notes',
            'tp_insurer_name': 'third_party__insurer__name',
        }

        if field.startswith('-'):
            mapped_field = f'-{fields.get(field[1:])}'
        else:
            mapped_field = fields.get(field)

        return mapped_field

    def get_ordering(self, request, queryset, view):
        params = request.query_params.get(self.ordering_param)
        if params:
            fields = [
                self._field_mapper(param.strip())
                for param in params.split(',')
            ]
            ordering = self.remove_invalid_fields(queryset, fields, view,
                                                  request)
            if ordering:
                return ordering

        return self.get_default_ordering(view)
