# Generated by Django 4.1.7 on 2023-05-26 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 5, 26, 14, 4, 6, 940983, tzinfo=datetime.timezone.utc), verbose_name='Date of publishing'),
            preserve_default=False,
        ),
    ]
