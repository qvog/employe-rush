from allauth.account.forms import LoginForm, SignupForm

from .models import Employer, Worker, CustomUser

class EmployerSignupForm(SignupForm):

    class Meta:
        model = Employer

    def custom_signup(self, request, user):
        user.type = CustomUser.Types.EMPLOYER
        user.save()        


class WorkerSignupForm(SignupForm):

    class Meta:
        model = Worker

    def type_worker(self, request, user):
        user.type = CustomUser.Types.WORKER
        user.save()
