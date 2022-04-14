from django import forms
from django.contrib.auth import get_user_model

from squandered.common.helpers import BootstrapFormMixin
from squandered.transaction.models import Expense, ExpenseCategory, IncomeCategory, Income

UserModel = get_user_model()


class BaseTransactionForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_form_control()
        self.user = user

    def save(self, commit=True):
        result = super().save(commit=False)
        result.user = self.user
        if commit:
            result.save()
        return result


class BaseTransactionCategoryForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_form_control()
        self.user = user

    def save(self, commit=True):
        category = super().save(commit=False)
        category.user = self.user
        if commit:
            category.save()
        return category


class AddExpenseForm(BaseTransactionForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields['category'].queryset = self.user.expensecategory_set.all()

    class Meta:
        model = Expense
        exclude = ('user',)


class AddIncomeForm(BaseTransactionForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields['category'].queryset = self.user.incomecategory_set.all()

    class Meta:
        model = Income
        exclude = ('user',)


class AddExpenseCategoryForm(BaseTransactionCategoryForm):
    class Meta:
        model = ExpenseCategory
        exclude = ('user',)


class AddIncomeCategoryForm(BaseTransactionCategoryForm):
    class Meta:
        model = IncomeCategory
        exclude = ('user',)
