from django.conf import settings

from vacancies.serializers import VacancySerializer
from vacancies.models import Vacancy


class Storage:
    def __init__(self, request):
        self.session = request.session
        storage = self.session.get(settings.STORAGE_SESSION_ID)
        if not storage:
            storage = self.session[settings.STORAGE_SESSION_ID] = {}
        self.storage = storage

    def save(self):
        self.session.modified = True

    def add(self, vacancies_id):
        vacancies_id = str(vacancies_id)
        if vacancies_id not in self.storage:
            self.storage[vacancies_id] = {
                "id": vacancies_id,
            }

        self.save()

    def remove(self, vacancies):
        vacancies_id = str(vacancies["id"])

        if vacancies_id in self.cart:
            del self.cart[vacancies_id]
            self.save()

    def __iter__(self):
        vacancies_ids = self.storage.keys()
        vacancies = Vacancy.objects.filter(id__in=vacancies_ids)
        storage = self.storage.copy()
        for vacancy in vacancies:
            storage[str(vacancy.id)]['vacancies'] = VacancySerializer(vacancy).data
        for item in storage.values():
            yield item

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()