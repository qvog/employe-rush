from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from PIL import Image


class CustomUser(AbstractUser):
    class Types(models.TextChoices):
        EMPLOYER = "EMPLOYER", "Employer"
        WORKER = "WORKER", "Worker"

    base_type = Types.WORKER
    type = models.CharField(max_length=50, choices=Types.choices, default=base_type)
    avatar = models.ImageField(upload_to='profile_images')

    def get_absolute_url(self):
        return reverse("users_detail", kwargs={"username": self.username})
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)
      
class EmployerManager(models.Manager):
    def normalize_email(self, email):
        return BaseUserManager.normalize_email(email)
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=CustomUser.Types.EMPLOYER)

class Employer(CustomUser):
    base_type = CustomUser.Types.EMPLOYER
    objects = EmployerManager()

    @property
    def more(self):
        return self.employermore
    
    class Meta:
        proxy = True

class EmployerMore(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    social = models.CharField(max_length=150, blank=True)
    areas_of_activity = models.CharField(max_length=150, blank=True)
    about = models.CharField(max_length=1024, blank=True)
    rate = models.FloatField([MinValueValidator(0.0), MaxValueValidator(10.0)], default=0)

    def __str__(self):
        return self.user.username

class WorkerManager(models.Manager):
    def normalize_email(self, email):
        return BaseUserManager.normalize_email(email)
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=CustomUser.Types.WORKER)

class Worker(CustomUser):
    base_type = CustomUser.Types.WORKER
    objects = WorkerManager()

    @property
    def more(self):
        return self.workermore

    class Meta:
        proxy = True

class WorkerMore(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    city = models.CharField(max_length=150, blank=True)
    ready_to_relocate = models.BooleanField(default=True, blank=True)
    position = models.CharField(max_length=150, blank=True)
    bio = models.CharField(max_length=512, blank=True)

    github_username = models.CharField(max_length=256, blank=True, db_index=True, default="")
    telegram_username = models.CharField(max_length=256, blank=True, db_index=True, default="")

    def __str__(self):
        return self.user.username



