from django.conf import settings
from django.core.cache import cache

from vacancies.serializers import VacancySerializer
from vacancies.models import Vacancy


class Storage:
    def __init__(self, user):
        self.user = user
        self.cache_key = f"storage_{user.id}"
        self.storage = cache.get(self.cache_key, {})

    def __iter__(self):
        vacancies_ids = self.storage.keys()
        vacancies = Vacancy.objects.filter(id__in=vacancies_ids)
        storage = self.storage.copy()

        for vacancy in vacancies:
            storage[str(vacancy.id)]['vacancies'] = VacancySerializer(vacancy).data
            
        for item in storage.values():
            yield item

    def save(self):
        cache.set(self.cache_key, self.storage, settings.CACHE_TIMEOUT)

    def add(self, vacancies_id):
        vacancies_id = str(vacancies_id)

        if vacancies_id not in self.storage:
            self.storage[vacancies_id] = {
                "id": vacancies_id,
            }

        self.save()

    def remove(self, vacancies_id):
        vacancies_id = str(vacancies_id)

        if vacancies_id in self.storage:
            del self.storage[vacancies_id]
            self.save()

    def clear(self):
        cache.delete(self.cache_key)
    
    
        