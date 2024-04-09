from django.contrib import admin

from core.admin.forms import CaseAdminForm
from core.admin.inlines import ExternalPartyServiceInline
from core.models import Case


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    form = CaseAdminForm
    inlines = [ExternalPartyServiceInline, ]
