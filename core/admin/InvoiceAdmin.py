from django.contrib import admin

from core.models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass
