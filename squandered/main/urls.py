from django.urls import path

from squandered.main import views

urlpatterns = (
    path('', views.IndexView.as_view(), name='index'),
)
