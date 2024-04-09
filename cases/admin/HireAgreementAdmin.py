from django.contrib import admin

from cases.models import HireAgreement


@admin.register(HireAgreement)
class HireAgreementAdmin(admin.ModelAdmin):
    pass
