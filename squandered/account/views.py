from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views

from squandered.account.forms import CustomUserRegisterForm, ProfileLoginForm
from squandered.account.models import Profile


class ProfileDetailView(views.DetailView):
    template_name = 'account/profile_details.html'
    model = Profile
    context_object_name = 'profile'


class ProfileRegisterView(views.CreateView):
    template_name = 'account/profile-register.html'
    form_class = CustomUserRegisterForm

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.id})


class ProfileLoginView(auth_views.LoginView):
    template_name = 'account/login.html'
    form_class = ProfileLoginForm

    def get_success_url(self):
        return reverse_lazy('index')


class ProfileLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('profile login')
