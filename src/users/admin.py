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
    list_display = ('username', 'email', 'id')
    readonly_fields = ('id',)
    admin.site.register(EmployerMore)

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'id')
    readonly_fields = ('id',)
    admin.site.register(WorkerMore)
