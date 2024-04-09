from django.contrib import admin

from core.models import Expense


class ExpenseInline(admin.TabularInline):
    model = Expense
