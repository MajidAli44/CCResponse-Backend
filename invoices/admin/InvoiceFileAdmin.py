from django.contrib import admin

from invoices.models import InvoiceFile


@admin.register(InvoiceFile)
class InvoiceFileAdmin(admin.ModelAdmin):
    pass
