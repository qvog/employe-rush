from django.db import models
from users.models import Worker
from vacancies.models import Vacancy

class SavedJobs(models.Model):
    worker = models.OneToOneField(Worker, on_delete=models.CASCADE)
    Vacancy = models.ManyToManyField(Vacancy)

    def add(self):
        pass

    def remove(self):
        pass

    
    
