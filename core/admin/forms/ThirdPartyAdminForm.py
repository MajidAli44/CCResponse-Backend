from django import forms

from core.models import Vehicle, ExternalParty


class ThirdPartyAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['insurer'].queryset = ExternalParty.objects.filter(role=ExternalParty.Role.insurer,
                                                                       is_third_party=True)
        self.fields['vehicle'].queryset = Vehicle.objects.filter(owner=Vehicle.Owner.third_party)
