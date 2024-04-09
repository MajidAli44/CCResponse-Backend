from rest_framework.serializers import ModelSerializer

from core.models import Case


class CasePartialSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super().__init__(*args, **kwargs)

    class Meta:
        model = Case
        fields = ('instruction_date', 'date_of_accident', 'time_of_accident', 'location',
                  'circumstances', 'other_info', 'weather', 'status', 'instruction_date',
                  'date_retained', 'payment_status', 'ack_comms', 'communication', 'should_show_hire_sr')
