from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

from .storage import Storage
from users.mixins import WorkerRequiredMixin, EmployerRequiredMixin


class StoragePageView(WorkerRequiredMixin, APIView):
    permission_classes = [IsAuthenticated]
    context_object_name = 'storage'

    def get(self, request):
        storage = Storage(request.user)

        context = {
            'storage': storage
        }
        
        return render(request, 'storage/savedvacancies.html', context)

    def post(self, request, *args, **kwargs):
        storage = Storage(request.user)

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
        storage = Storage(request.user)

        context = {
            'storage': storage
        }
        
        return render(request, 'storage/replyes.html', context)