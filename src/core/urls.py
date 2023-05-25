from django.urls import path

from core.views import FrontPageView

urlpatterns = [
    path('', FrontPageView.as_view(), name='frontpage'),
]
