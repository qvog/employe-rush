from django.urls import path, include
from django.contrib.auth import views

from users.views import (
    WorkerSignupView, 
    WorkerLoginView, 
    WorkerProfile,
    WorkerProfileEdit, 
    EmployerProfile, 
    EmployerSignupView,
    EmployerProfileEdit
    )


app_name = 'users'

urlpatterns = [
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('signup/', WorkerSignupView.as_view(), name='work_signup'),
    path('login/', WorkerLoginView.as_view(), name='work_login'),
    path('profile', WorkerProfile.as_view(), name='work_profile'),
    path('profile/edit', WorkerProfileEdit.as_view(), name='work_editprofile'),

    path('signup/emp/', EmployerSignupView.as_view(), name='emp_signup'),
    path('profile/emp/', EmployerProfile.as_view(), name='emp_profile'),
    path('profile/emp/edit', EmployerProfileEdit.as_view(), name='emp_editprofile'),
]

