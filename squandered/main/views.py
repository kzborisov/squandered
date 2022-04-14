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

        expenses_per_month = expenses. \
            annotate(month=TruncMonth('date')). \
            values('month'). \
            annotate(total_expense=Sum('amount')). \
            order_by('date__month')

        transactions = expenses_per_month

        for t in transactions:
            try:
                t['total_income'] = incomes.filter(date__month=t['month'].month). \
                    annotate(month=TruncMonth('date')). \
                    values('month'). \
                    annotate(total=Sum('amount'))[0]['total']
            except IndexError:
                t['total_income'] = 0
        context['monthy_transactions'] = transactions

        context['spent_per_category'] = expenses. \
            values('category__name'). \
            annotate(total=Sum('amount'))

        total_spent = expenses.aggregate(Sum('amount'))
        total_spent = total_spent['amount__sum']
        context['total_spent'] = total_spent if total_spent else 0

        total_income = incomes.aggregate(Sum('amount'))
        total_income = total_income['amount__sum']
        context['total_income'] = total_income if total_income else 0

        labels = []
        data = []

        for category in context['spent_per_category']:
            labels.append(category['category__name'])
            data.append(float(category['total']))

        months = []
        expenses = []
        income = []
        for t in transactions:
            months.append(t['month'].strftime("%B"))
            expenses.append(float(t['total_expense']))
            income.append(float(t['total_income']))

        context['months'] = months
        context['expenses'] = expenses
        context['labels'] = labels
        context['data'] = data
        return context
