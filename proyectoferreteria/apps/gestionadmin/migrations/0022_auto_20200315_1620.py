# Generated by Django 2.2.6 on 2020-03-15 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0021_auto_20200315_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnoempleado',
            name='horaEntrada',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='turnoempleado',
            name='horaSalida',
            field=models.TimeField(),
        ),
    ]
