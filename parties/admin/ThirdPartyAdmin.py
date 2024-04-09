from django.contrib import admin

from parties.models import ThirdParty


@admin.register(ThirdParty)
class ThirdPartyAdmin(admin.ModelAdmin):
    pass
