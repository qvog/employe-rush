from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import VacancySerializer
from django.views.generic import ListView, DetailView, TemplateView


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

        context = {
            'vacancies': vacancies,
        }

        return render(request, 'vacancies/vacancies.html', context)

class VacancyDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, vacancy_id):
        vacancy = Vacancy.objects.get(id=vacancy_id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

class SavedVacanciesView(TemplateView):
    template_name = 'vacancies/savedvacancies.html'
    
    def get(self, request):
        new_fil = Vacancy.objects.filter(salary=60000)
        context = {
            'new_fil': new_fil,
        }
        return render(request, 'vacancies/savedvacancies.html', context)
    

    