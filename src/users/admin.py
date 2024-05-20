from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 

from users.models import (
    Employer, 
    EmployerMore,
    Worker,
    WorkerMore,
)

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    admin.site.register(EmployerMore)

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    admin.site.register(WorkerMore)
