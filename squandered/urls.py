from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('squandered.main.urls')),
    path('profile/', include('squandered.account.urls')),
    path('transaction/', include('squandered.transaction.urls')),
]
