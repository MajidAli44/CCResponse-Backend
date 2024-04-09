from django import forms

from core.models import ExternalParty


class ExternalPartyServiceAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExternalPartyServiceAdminForm, self).__init__(*args, **kwargs)
        self.fields['external_party'].queryset = ExternalParty.objects.filter(is_third_party=False)
