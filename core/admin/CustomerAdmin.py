from django.contrib import admin

from core.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
