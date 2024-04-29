# Generated by Django 5.0.4 on 2024-04-27 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_employermore_workermore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=models.CharField(choices=[('EMPLOYER', 'Employer'), ('WORKER', 'Worker')], max_length=50),
        ),
    ]
