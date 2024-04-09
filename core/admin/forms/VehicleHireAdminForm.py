from django import forms

from core.models import Vehicle


class VehicleHireAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vehicle'].queryset = Vehicle.objects.filter(owner=Vehicle.Owner.company)
