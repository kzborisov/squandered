from django.urls import path

from squandered.transaction import views

urlpatterns = (
    path('add-expense/', views.AddExpenseView.as_view(), name='add expense'),
    path('add-expense-category/', views.AddExpenseCategoryView.as_view(), name='add expense category'),
    path('add-income/', views.AddIncomeView.as_view(), name='add income'),
    path('add-income-category/', views.AddIncomeCategoryView.as_view(), name='add income category'),
    path('expenses-details/', views.ExpensesDetailsView.as_view(), name='expenses details'),
    path('income-details/', views.IncomeDetailsView.as_view(), name='income details')
)
