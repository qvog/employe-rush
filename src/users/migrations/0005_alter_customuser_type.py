# Generated by Django 5.0.4 on 2024-04-27 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=models.CharField(choices=[('EMPLOYER', 'Employer'), ('WORKER', 'Worker')], default='EMPLOYER', max_length=50),
        ),
    ]
