from django.db import models
from django.conf import settings

from vacancies.models import Vacancy

class DefaultStorage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'vacancy')

class ReplyeStorage(DefaultStorage):
    class Meta:
        pass








