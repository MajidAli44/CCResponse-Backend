from django.contrib import admin

from core.admin.forms import ExternalPartyServiceAdminForm
from core.models import ExternalPartyService


class ExternalPartyServiceInline(admin.TabularInline):
    model = ExternalPartyService
    form = ExternalPartyServiceAdminForm
