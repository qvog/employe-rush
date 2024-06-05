from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .storage import Storage
from .models import EmployerStorage
from users.mixins import WorkerRequiredMixin


class StoragePageView(WorkerRequiredMixin, APIView):
    permission_classes = [IsAuthenticated]
    context_object_name = 'storage'

    def get(self, request):
        storage = Storage(request)

        context = {
            'storage': storage
        }
        
        return render(request, 'storage/savedvacancies.html', context)
    
    def post(self, request, *args, **kwargs):
        storage = Storage(request)

        if request.POST.get('action') == 'add':
            vacancy_id = request.POST.get('vacancy')
            storage.add(vacancy_id)
            response = render(request, 'storage/savedvacancies.html')
        elif request.POST.get('action') == 'remove':
            vacancy_id = request.POST.get('vacancy')
            storage.remove(vacancy_id)
            response = render(request, 'storage/savedvacancies.html')
        elif request.POST.get('action' == 'reply'):
            employer_storage = EmployerStorage(request)
            vacancy_id = request.POST.get('vacancy')
            employer_storage.add(vacancy_id)
            response = render(request, 'users/employer/replyes.html')

        return response

class EmployerReplyesView(APIView):
    permission_classes = [IsAuthenticated]
    context_object_name = 'employer_storage'

    def get(self, request):
        employer_storage = EmployerStorage(request)

        context = {
            'employer_storage': employer_storage
        }
        
        return render(request, 'users/employer/replyes.html', context)