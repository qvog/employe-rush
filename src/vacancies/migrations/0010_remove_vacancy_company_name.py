# Generated by Django 5.0.4 on 2024-05-17 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0009_vacancy_employer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='company_name',
        ),
    ]