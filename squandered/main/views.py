from django.shortcuts import get_object_or_404
from django.views import generic as views

from squandered.account.models import Profile


class IndexView(views.TemplateView):
    template_name = 'main/index.html'


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if self.request.user.is_authenticated:
    #         context['profile'] = get_object_or_404(Profile, user__pk=self.request.user.id)
    #     return context
