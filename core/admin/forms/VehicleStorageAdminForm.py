from django import forms

from core.models import Vehicle


class VehicleStorageAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vehicle'].queryset = Vehicle.objects.filter(owner=Vehicle.Owner.company)
