from allauth.account.views import LoginView, SignupView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from django.views.generic import RedirectView, TemplateView

from users.forms import EmployerSignupForm, WorkerSignupForm

class EmployerSignupView(SignupView, TemplateView):
    template_name = 'users/employer/empsignup.html'
    form_class = EmployerSignupForm

    def get_context_data(self, **kwargs):
        kwargs['employer_form'] = EmployerSignupForm
        return super().get_context_data(**kwargs) 

class WorkerSignupView(SignupView, TemplateView):
    template_name = 'users/worker/worksignup.html'
    form_class = WorkerSignupForm

    def get_context_data(self, **kwargs):
        kwargs['worker_form'] = WorkerSignupForm
        return super().get_context_data(**kwargs) 

class WorkerLoginView(LoginView, TemplateView):
    template_name = 'users/worker/worklogin.html'

class WorkerProfile(LoginRequiredMixin, TemplateView):
    template_name = 'users/worker/workprofile.html'

class EmployerProfile(LoginRequiredMixin, TemplateView):
    template_name = 'users/employer/emprofile.html'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(
            "users:detail",
            kwargs={"username": self.request.user.username},
        )


