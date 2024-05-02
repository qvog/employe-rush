from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Vacancy
from .serializers import VacancySerializer


class VacanciesPageView(APIView):
    model = Vacancy
    permission_classes = [IsAuthenticated]
    context_object_name = 'vacancies'

    serializer_class = VacancySerializer

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

    def get(self, request, vacancy_id):
        vacancy = Vacancy.objects.get(id=vacancy_id)
        serializer = VacancySerializer(vacancy)

        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    
    
    
    

    