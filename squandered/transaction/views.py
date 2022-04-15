from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views

from squandered.transaction.forms import AddExpenseForm, AddExpenseCategoryForm, AddIncomeForm, AddIncomeCategoryForm
from squandered.transaction.models import Expense, Income


class BaseTransactionView(LoginRequiredMixin, views.CreateView):
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AddExpenseView(BaseTransactionView):
    form_class = AddExpenseForm
    template_name = 'transaction/add-expense.html'


class AddExpenseCategoryView(BaseTransactionView):
    form_class = AddExpenseCategoryForm
    template_name = 'transaction/add-expense-category.html'
    success_url = reverse_lazy('add expense')


class AddIncomeView(BaseTransactionView):
    form_class = AddIncomeForm
    template_name = 'transaction/add-income.html'


class AddIncomeCategoryView(BaseTransactionView):
    form_class = AddIncomeCategoryForm
    template_name = 'transaction/add-income-category.html'
    success_url = reverse_lazy('add income')


class ExpensesDetailsView(LoginRequiredMixin, views.ListView):
    template_name = 'transaction/expenses-details.html'
    model = Expense
    context_object_name = 'expenses'


class IncomeDetailsView(LoginRequiredMixin, views.ListView):
    template_name = 'transaction/income-details.html'
    model = Income
    context_object_name = 'incomes'