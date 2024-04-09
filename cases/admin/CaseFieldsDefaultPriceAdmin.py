from django.contrib import admin

from cases.models import CaseFieldsDefaultPrice


@admin.register(CaseFieldsDefaultPrice)
class CaseFieldsDefaultPriceAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if CaseFieldsDefaultPrice.objects.all().count() > 0:
            return False
        return super(CaseFieldsDefaultPriceAdmin, self).has_add_permission(request)
