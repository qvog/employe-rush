from django.shortcuts import redirect
from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter

class LogoutAccountAdapter(DefaultAccountAdapter):

    def get_logout_redirect_url(self, request):
        response = super().logout(request)
        return redirect('/')