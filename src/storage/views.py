from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .storage import Storage
from users.mixins import WorkerRequiredMixin, EmployerRequiredMixin


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
        elif request.POST.get('action') == ('reply'):
            vacancy_id = request.POST.get('vacancy')
            response = render(request, 'storage/savedvacancies.html')

        return response


class EmployerReplyesView(APIView):
    permission_classes = [IsAuthenticated]
    context_object_name = 'replye_storage'

    def get(self, request):

        storage = request(Storage)

        context = {
            'replye_storage': storage
        }
        
        return render(request, 'storage/replyes.html', context)