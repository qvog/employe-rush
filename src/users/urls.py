from django.urls import path, include
from django.contrib.auth import views

from users.views import UserRedirectView, EmployerSignupView, WorkerSignupView, WorkerLoginView, WorkerProfile, EmployerProfile

app_name = 'users'

urlpatterns = [
    path('signup/', WorkerSignupView.as_view(), name='worksignup'),
    path('signup/emp/', EmployerSignupView.as_view(), name='empsignup'),
    path('login/', WorkerLoginView.as_view(), name='worklogin'),
    path('~redirect/', UserRedirectView.as_view(), name="redirect"),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('profile/', WorkerProfile.as_view(), name='workprofile'),
    path('profile/emp/', EmployerProfile.as_view(), name='emprofile'),
]

