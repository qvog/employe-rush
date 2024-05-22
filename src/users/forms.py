from django.utils.translation import gettext_lazy as _
from allauth.account.forms import SignupForm
from django import forms

from .models import CustomUser, WorkerMore, EmployerMore


class EmployerSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def custom_signup(self, request, user):
        user.type = CustomUser.Types.EMPLOYER
        user.save()

class EmployerUpdateForm(forms.ModelForm):
    pass
        
class WorkerSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def custom_signup(self, request, user):
        user.type = CustomUser.Types.WORKER
        user.save()


class UpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']

class WorkerUpdateFormMore(forms.ModelForm):
    city = forms.CharField(max_length=150, required=False)
    ready_to_relocate = forms.BooleanField(required=False)
    position = forms.CharField(max_length=150, required=False)
    bio = forms.CharField(max_length=512, required=False)
    telegram_username = forms.CharField(max_length=256, required=False)
    github_username = forms.CharField(max_length=256, required=False)
    
    class Meta:
        model = WorkerMore
        fields = ['city', 'ready_to_relocate', 'position', 'bio', 'github_username', 'telegram_username',]

class EmployerUpdateFormMore(forms.ModelForm):
    city = forms.CharField(max_length=150, required=False)
    ready_to_relocate = forms.BooleanField(required=False)
    position = forms.CharField(max_length=150, required=False)
    bio = forms.CharField(max_length=512, required=False)
    telegram_username = forms.CharField(max_length=256, required=False)
    github_username = forms.CharField(max_length=256, required=False)
    
    class Meta:
        model = EmployerMore
        fields = ['city', 'ready_to_relocate', 'position', 'bio', 'github_username', 'telegram_username',]
    
