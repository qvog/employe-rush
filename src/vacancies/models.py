from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    class EXPERIENCE(models.TextChoices):
        INEXPERIENCED = "NOEXP", _("Без опыта")
        INTERN = "INTERN", _("После стажировки")
        ONEYEAR = "1TO3", _("От 1 года до 3 лет")
        THREEYEAR = "3TO6", _("От 3 лет до 6 лет")
        SIXYEAR = "SIX", _("Более 6 лет")
    class JOBTYPE(models.TextChoices):
        FULL = "FULL", _("Full-time")
        PART = "PART", _("Part-time")
        TRAINEE = "TRAINEE", _("Стажировка")
        TEMPORARY = "TEMPORARY", _("Временно")

    category = models.ForeignKey(Category, related_name='vacancies', on_delete=models.CASCADE, null=True)
    name = models.CharField(_("Name of vacancie"), max_length=50, null=True)
    city = models.CharField(_("The city of job"), max_length=50, null=True)
    salary = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)
    discription = models.TextField(max_length=600, null=True)
    workhome = models.BooleanField(_("Work from home or not"), default=False)

    experience = models.CharField(max_length=20, choices=EXPERIENCE.choices, blank=True)
    jobtype = models.CharField(max_length=20, choices=JOBTYPE.choices, blank=True)

    def __str__(self):
        return self.name