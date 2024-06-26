from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from users.models import EmployerMore

class Category(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    class EXPERIENCE(models.TextChoices):
        INEXPERIENCED = "NOEXP", _("Без опыта")
        INTERN = "INTERN", _("После стажировки")
        ONEYEAR = "1TO3", _("От 1 до 3 лет")
        THREEYEAR = "3TO6", _("От 3 до 6 лет")
        SIXYEAR = "SIX", _("Более 6 лет")
    class JOBTYPE(models.TextChoices):
        FULL = "FULL", _("Full-time")
        PART = "PART", _("Part-time")
        TRAINEE = "TRAINEE", _("Стажировка")
        TEMPORARY = "TEMPORARY", _("Временно")

    category = models.ForeignKey(Category, related_name='vacancies', on_delete=models.CASCADE, null=True)
    employer = models.ForeignKey(EmployerMore, related_name='employer', on_delete=models.CASCADE, null=True)
    name = models.CharField(_("Name of vacancy"), max_length=30, null=True)
    city = models.CharField(_("The city of job"), max_length=30, null=True)
    salary = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)
    description = models.TextField(max_length=1200, null=True)
    workhome = models.BooleanField(_("Work from home"), default=False)
    created_at = models.DateTimeField(_("Date of publishing"), auto_now_add=True)

    experience = models.CharField(max_length=20, choices=EXPERIENCE.choices, blank=True)
    jobtype = models.CharField(max_length=20, choices=JOBTYPE.choices, blank=True)
    
    class Meta:
        ordering = ('-created_at', )  

    def __str__(self):
        return f'{self.name} {self.employer}'
    