from django.urls import path, include
from django.contrib.auth import views

from storage.views import StoragePageView

app_name = 'storage'

urlpatterns = [
    path('', StoragePageView.as_view(), name='savedvacancies.html'),
]