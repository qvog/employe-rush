from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import WorkerMore, EmployerMore

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        WorkerMore.objects.create(user=instance)
        print('succes')

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.workermore.save()

