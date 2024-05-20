# Generated by Django 5.0.4 on 2024-05-16 07:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_customuser_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employermore',
            name='testfield',
        ),
        migrations.AddField(
            model_name='employermore',
            name='about',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='employermore',
            name='areas_of_activity',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='employermore',
            name='rate',
            field=models.FloatField(default=0, verbose_name=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
        migrations.AddField(
            model_name='employermore',
            name='social',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
