# Generated by Django 5.0.4 on 2024-05-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_workermore_testfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
        migrations.RemoveField(
            model_name='workermore',
            name='testfield',
        ),
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='profile_images'),
        ),
        migrations.AddField(
            model_name='workermore',
            name='bio',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='workermore',
            name='city',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='workermore',
            name='position',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='workermore',
            name='ready_to_relocate',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]