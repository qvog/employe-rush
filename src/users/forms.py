from django import forms as d_forms
from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model, forms

from .models import CustomUser


User = get_user_model()

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User

class EmployerSignupForm(SignupForm):

    def custom_signup(self, request, user):
        user.type = CustomUser.Types.EMPLOYER
        user.save()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class WorkerSignupForm(SignupForm):

    def custom_signup(self, request, user):
        user.type = CustomUser.Types.WORKER
        user.save()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
