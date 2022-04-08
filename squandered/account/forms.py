from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model

from squandered.account.models import Profile
from squandered.common.helpers import RemoveHelpTextMixin, BootstrapFormMixin


class CustomUserRegisterForm(RemoveHelpTextMixin, BootstrapFormMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_help_text()
        self._apply_form_control()

    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
        required=False,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
        required=False,
    )

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            user=user,
        )
        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']


class ProfileLoginForm(BootstrapFormMixin, auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_form_control()
