from django.urls import path

from vacancies.views import VacanciesPageView, VacancyDetailView, SavedVacanciesView

app_name = 'vacancies'

urlpatterns = [
    path('', VacanciesPageView.as_view(), name='vacancies'),
    path('<int:vacancy_id>', VacancyDetailView.as_view(), name='vacancies_detail'),
    path('savedvacancies', SavedVacanciesView.as_view(), name='savedvacancies'),
]
