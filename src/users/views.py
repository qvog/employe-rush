from allauth.account.views import LoginView, SignupView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages

from users.forms import EmployerSignupForm, WorkerSignupForm, UpdateForm, WorkerUpdateFormMore


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

    def post(self, request):
        user_form = UpdateForm(request.POST, instance=request.user)
        worker_form = EmployerUpdateFormMore(request.POST, instance=request.user.employermore)
        if user_form.is_valid() and worker_form.is_valid():
            user_form.save()
            worker_form.save()
            return redirect(to='users:work_profile')
        else:
            print('not valid')

        return render(request, 'users/worker/work_editprofile.html')

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
    
    def post(self, request):
        user_form = UpdateForm(request.POST, instance=request.user)
        worker_form = WorkerUpdateFormMore(request.POST, instance=request.user.workermore)
        if user_form.is_valid() and worker_form.is_valid():
            user_form.save()
            worker_form.save()
            return redirect(to='users:work_profile')
        else:
            print('not valid')

        return render(request, 'users/worker/work_editprofile.html')
            





