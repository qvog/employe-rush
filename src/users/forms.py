from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth import get_user_model, forms
from django.http import HttpResponse

from .models import Employer, Worker, CustomUser

User = get_user_model()

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User

class EmployerSignupForm(SignupForm):

    class Meta:
        model = Employer
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def type_employer(self, request, user):
        user.type = CustomUser.Types.EMPLOYER
        user.save()
        return HttpResponse(print('pizda'))    

class WorkerSignupForm(SignupForm):

    class Meta:
        model = Worker

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def type_worker(self, user):
        user.type = CustomUser.Types.WORKER
        user.save()
