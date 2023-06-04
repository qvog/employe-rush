from django.urls import path

from vacancies.views import VacanciesPageView, VacancyDetailView

app_name = 'vacancies'

urlpatterns = [
    path('', VacanciesPageView.as_view(), name='vacancies'),
    path('<int:vacancy_id>', VacancyDetailView.as_view(), name='vacancies_detail'),
]
