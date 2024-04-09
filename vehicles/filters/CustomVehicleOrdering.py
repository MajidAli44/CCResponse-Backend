from rest_framework.filters import OrderingFilter


class CustomVehicleOrdering(OrderingFilter):
    """Custom ordering class for vehicle list with field mapper"""

    def _field_mapper(self, field):
        fields = {
            'registration': 'registration',
            'client_name': 'hire_details__case__client__name',
            'make_model': 'make_model',
            'start_date': 'hire_details__case__start_date',
            'mot_expiry': 'mot_expiry',
            'tax_expiry': 'tax_expiry',
            'service_due': 'service_due',
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
