from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Vacancy, Category

# Create your views here.
class VacanciesPageView(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'
    context_object_name = 'vacancies'