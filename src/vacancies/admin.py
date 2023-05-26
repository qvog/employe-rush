from django.contrib import admin

from .models import Vacancy, Category

admin.site.register(Category)
admin.site.register(Vacancy)