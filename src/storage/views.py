from django.shortcuts import render
from .storage import Storage

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StorageAPI(APIView):
    def get(self, request, format=None):
        storage = Storage(request)

        return Response ({"data": (storage.__iter__())},
            status=status.HTTP_200_OK)
    
    def post(self, request, **kwargs):
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