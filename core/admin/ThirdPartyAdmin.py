from django.contrib import admin

from core.admin.forms import ThirdPartyAdminForm
from core.models import ThirdParty


@admin.register(ThirdParty)
class ThirdPartyAdmin(admin.ModelAdmin):
    form = ThirdPartyAdminForm
