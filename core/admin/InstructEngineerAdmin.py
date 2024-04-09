from django.contrib import admin

from core.models import InstructEngineer


@admin.register(InstructEngineer)
class InstructEngineerAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return InstructEngineer.objects.count() < 1
