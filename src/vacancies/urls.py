from django.urls import path

from vacancies.views import VacanciesPageView, VacancyDetailAPI

app_name = 'vacancies'

urlpatterns = [
    path('', VacanciesPageView.as_view(), name='vacancies'),
    path('<int:vacancy_id>', VacancyDetailAPI.as_view(), name='vacancies_detail'),
]
