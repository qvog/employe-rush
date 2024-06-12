from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .storage import Storage
from .models import DefaultStorage, ReplyeStorage
from users.mixins import WorkerRequiredMixin, EmployerRequiredMixin


class StoragePageView(WorkerRequiredMixin, APIView):
    permission_classes = [IsAuthenticated]
    context_object_name = 'storage'

    def get(self, request):
        user = request.user
        
        default_storage = DefaultStorage.objects.filter(user=user)
        storage = [item.vacancy for item in default_storage]

        context = {
            'storage': storage
        }
        
        return render(request, 'storage/savedvacancies.html', context)

    def post(self, request, *args, **kwargs):
        storage = Storage(request)
        user = request.user

        if request.POST.get('action') == 'add':
            vacancy_id = request.POST.get('vacancy')
            storage.add(vacancy_id)
            storage.transfer_to_db(user)
            response = render(request, 'storage/savedvacancies.html')
        elif request.POST.get('action') == 'remove':
            vacancy_id = request.POST.get('vacancy')
            storage.remove(user, vacancy_id)
            response = render(request, 'storage/savedvacancies.html')
        elif request.POST.get('action' == 'reply'):
            vacancy_id = request.POST.get('vacancy')
            response = render(request, 'users/employer/replyes.html')

        return response


class EmployerReplyesView(EmployerRequiredMixin, APIView):
    permission_classes = [IsAuthenticated]
    context_object_name = 'replye_storage'

    def get(self, request):
        user = request.user
        
        replye_storage = ReplyeStorage.objects.filter(user=user)
        storage = [item.vacancy for item in replye_storage]

        context = {
            'replye_storage': storage
        }
        
        return render(request, 'users/employer/replyes.html', context)
