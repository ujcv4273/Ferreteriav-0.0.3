# Generated by Django 2.2.6 on 2020-03-15 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0026_auto_20200315_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnoempleado',
            name='horaEntrada',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='turnoempleado',
            name='horaSalida',
            field=models.CharField(max_length=5),
        ),
    ]
