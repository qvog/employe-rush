from allauth.account.views import LoginView, SignupView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from django.views.generic import RedirectView, TemplateView

from users.forms import EmployerSignupForm, WorkerSignupForm

class EmployerSignupView(SignupView, TemplateView):
    template_name = 'users/empsignup.html'
    form_class = EmployerSignupForm

class WorkerSignupView(SignupView, TemplateView):
    template_name = 'users/worksignup.html'
    form_class = WorkerSignupForm

class WorkerLoginView(LoginView, TemplateView):
    template_name = 'users/worklogin.html'

class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(
            "users:detail",
            kwargs={"username": self.request.user.username},
        )


