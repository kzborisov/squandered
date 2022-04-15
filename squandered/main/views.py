from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.views import generic as views

from squandered.transaction.models import Expense, Income


class IndexView(views.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        expenses = Expense.objects.filter(user__id=self.request.user.id)
        incomes = Income.objects.filter(user__id=self.request.user.id)

        context['monthly_transactions'] = expenses. \
            annotate(month=TruncMonth('date')). \
            values('month'). \
            annotate(total_expense=Sum('amount')). \
            order_by('date__month')

        context['spent_per_category'] = expenses. \
            values('category__name'). \
            annotate(total=Sum('amount'))

        context['income_per_category'] = incomes.values('category__name').annotate(total=Sum('amount'))

        total_spent = expenses.aggregate(Sum('amount'))
        total_spent = total_spent['amount__sum']
        context['total_spent'] = total_spent if total_spent else 0

        total_income = incomes.aggregate(Sum('amount'))
        total_income = total_income['amount__sum']
        context['total_income'] = total_income if total_income else 0

        expense_categories = []
        total_expense_per_category = []

        for category in context['spent_per_category']:
            expense_categories.append(category['category__name'])
            total_expense_per_category.append(float(category['total']))

        context['expense_categories'] = expense_categories
        context['total_expense_per_category'] = total_expense_per_category

        income_categories = []
        total_income_per_category = []

        for category in context['income_per_category']:
            income_categories.append(category['category__name'])
            total_income_per_category.append(float(category['total']))

        context['income_categories'] = income_categories
        context['total_income_per_category'] = total_income_per_category

        return context
