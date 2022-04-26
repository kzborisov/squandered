from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.http import Http404
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


class TransactionDetailsPerMonthView(LoginRequiredMixin, views.ListView):
    model = Expense
    context_object_name = 'expenses'
    template_name = 'transaction/transactions-per-month.html'

    def dispatch(self, request, *args, **kwargs):
        if self.kwargs['month'] not in range(1, 13):
            raise Http404("Invalid month")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user.id).filter(date__month=self.kwargs['month'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_year = date.today().year
        incomes = Income.objects. \
            filter(user_id=self.request.user.id). \
            filter(date__month=self.kwargs['month']).filter(date__year=current_year)

        total_expenses = self.get_queryset().values('amount').aggregate(Sum('amount'))
        total_income = incomes.values('amount').aggregate(Sum('amount'))
        total_income['amount__sum'] = total_income['amount__sum'] if total_income['amount__sum'] else 0

        context['month'] = self.kwargs['month']
        context['incomes'] = incomes

        context['total_expense'] = total_expenses
        context['total_income'] = total_income

        context['balance'] = total_income['amount__sum'] - total_expenses['amount__sum']

        return context
