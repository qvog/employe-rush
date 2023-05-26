from django.urls import path

from vacancies.views import VacanciesPageView

urlpatterns = [
    path('', VacanciesPageView.as_view(), name='vacancies'),
]
