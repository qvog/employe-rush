from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from .models import Vacancy

class VacanciesPageView(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'
    context_object_name = 'vacancies'

class VacancyDetailView(DetailView):
    model = Vacancy
    def get(self, request, vacancy_id):
        vacancy = Vacancy.objects.get(pk=vacancy_id)
        data = {
            'name': vacancy.name,
            'company_name': vacancy.company_name,
            'city': vacancy.city,
            'description': vacancy.description,
            'salary': vacancy.salary,
            'experience': vacancy.experience,
            'jobtype': vacancy.jobtype
        }
        return JsonResponse(data)