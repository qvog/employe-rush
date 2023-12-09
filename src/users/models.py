from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    class Types(models.TextChoices):
        EMPLOYER = "EMPLOYER", "Employer"
        WORKER = "WORKER", "Worker"

    base_type = Types.WORKER

    type = models.CharField(max_length=50, choices=Types.choices, default=base_type)

    name = models.CharField(blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"username": self.username})
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)
    
class EmployerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=CustomUser.Types.EMPLOYER)
      
class WorkerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=CustomUser.Types.WORKER)

class Employer(CustomUser):
    base_type = CustomUser.Types.EMPLOYER
    objects = EmployerManager()
    
    class Meta:
        proxy = True

class Worker(CustomUser):
    base_type = CustomUser.Types.WORKER
    objects = WorkerManager()

    class Meta:
        proxy = True


