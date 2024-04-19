from .storage import Storage

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class StorageAPI(APIView):
    permission_classes = [IsAuthenticated]
    context_object_name = 'storage'

    def get(self, request):
        storage = Storage(request)

        context = {
            'storage': storage,
        }
        
        return render(request, 'storage/savedvacancies.html', context)
    
    def post(self, request, **kwargs):
        storage = Storage(request)

        if request.POST.get('action') == 'add':
            vacancy_id = request.POST.get('vacancy')
            storage.add(vacancy_id)
            response = render(request, 'storage/savedvacancies.html')
        elif request.POST.get('action') == 'remove':
            vacancy_id = request.POST.get('vacancy')
            storage.remove(vacancy_id)
            response = render(request, 'storage/savedvacancies.html')
        else:
            pass

        return response

        """
        storage = Storage(request)

        if "remove" in request.data:
            vacancies = request.data["vacancies"]
            storage.remove(vacancies)

        elif "clear" in request.data:
            storage.clear()

        else:
            vacancies = request.data
            storage.add(
                    vacancies=vacancies["vacancies"],
                    quantity=vacancies["quantity"]
                )

        return Response(
            {"message": "storage updated"},
            status=status.HTTP_202_ACCEPTED)
        """