from django.contrib import admin

from squandered.account.models import Profile, CustomUser


class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_staff')
    inlines = (ProfileInline,)
