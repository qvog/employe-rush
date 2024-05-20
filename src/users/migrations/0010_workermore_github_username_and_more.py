# Generated by Django 5.0.4 on 2024-05-09 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_customuser_name_remove_workermore_testfield_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workermore',
            name='github_username',
            field=models.CharField(blank=True, db_index=True, default='', max_length=256),
        ),
        migrations.AddField(
            model_name='workermore',
            name='telegram_username',
            field=models.CharField(blank=True, db_index=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='workermore',
            name='bio',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='workermore',
            name='city',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='workermore',
            name='position',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
