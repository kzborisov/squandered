from django.contrib import admin

from squandered.transaction.models import ExpenseCategory, Expense, IncomeCategory, Income


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'user')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'amount', 'date', 'created_at', 'user')


@admin.register(IncomeCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'user')


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'amount', 'date', 'created_at', 'user')
