from django import forms

from core.models import Vehicle


class CaseAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_vehicle'].queryset = Vehicle.objects.filter(owner=Vehicle.Owner.customer)
