from django.contrib import admin

from cases.models import UserDisplayCaseColumn


@admin.register(UserDisplayCaseColumn)
class UserDisplayCaseColumnAdmin(admin.ModelAdmin):
    pass
