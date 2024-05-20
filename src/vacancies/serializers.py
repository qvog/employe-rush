from rest_framework import serializers
from .models import Vacancy
from users.models import EmployerMore

class VacancySerializer(serializers.ModelSerializer):
    employer = serializers.StringRelatedField()
    class Meta:
        model = Vacancy
        fields = ('__all__')
