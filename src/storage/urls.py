from django.urls import path, include
from django.contrib.auth import views

from storage.views import StorageAPI

app_name = 'storage'

urlpatterns = [
    path('', StorageAPI.as_view(), name='savedvacancies.html'),
]