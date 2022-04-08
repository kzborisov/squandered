from django.urls import path

from squandered.account import views

urlpatterns = (
    path('details/<int:pk>/', views.ProfileDetailView.as_view(), name='profile details'),
    path('register/', views.ProfileRegisterView.as_view(), name='profile register'),
    path('login/', views.ProfileLoginView.as_view(), name='profile login'),
    path('logout/', views.ProfileLogoutView.as_view(), name='profile logout'),
)
