from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, View

from .models import Vacancy

class VacanciesPageView(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'
    context_object_name = 'vacancies'

    def get(self, request):
        query = request.GET.get('query', '')
        vacancies = Vacancy.objects.all()

        if query:
            vacancies = vacancies.filter(Q(name__icontains=query) | Q(description__icontains=query))

        context = {'vacancies': vacancies}
        return render(request, 'vacancies/vacancies.html', context)
    
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
    