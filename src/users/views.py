from allauth.account.views import LoginView, SignupView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, redirect


from users.forms import EmployerSignupForm, WorkerSignupForm
from .models import CustomUser


class EmployerSignupView(SignupView, TemplateView):
    template_name = 'users/employer/emp_signup.html'
    form_class = EmployerSignupForm

    def get_context_data(self, **kwargs):
        kwargs['employer_form'] = EmployerSignupForm
        return super().get_context_data(**kwargs)

class EmployerProfile(LoginRequiredMixin, TemplateView):
    template_name = 'users/employer/emp_profile.html'

class EmployerProfileEdit(LoginRequiredMixin, TemplateView):
    template_name = 'users/employer/emp_editprofile.html'
    
    def post(self, request, *args, **kwargs):
        user = request.user
        user.username = request.POST.get('username')
        user.save()
        #test branch
        return redirect('/')

class WorkerSignupView(SignupView, TemplateView):
    template_name = 'users/worker/work_signup.html'
    form_class = WorkerSignupForm

    def get_context_data(self, **kwargs):
        kwargs['worker_form'] = WorkerSignupForm
        return super().get_context_data(**kwargs)

class WorkerLoginView(LoginView, TemplateView):
    template_name = 'users/worker/work_login.html'

class WorkerProfile(LoginRequiredMixin, TemplateView):
    template_name = 'users/worker/work_profile.html'

class WorkerProfileEdit(LoginRequiredMixin, TemplateView):
    template_name = 'users/worker/work_editprofile.html'




