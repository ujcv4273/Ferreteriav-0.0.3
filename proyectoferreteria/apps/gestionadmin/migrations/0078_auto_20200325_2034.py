# Generated by Django 3.0.4 on 2020-03-26 02:34

from django.db import migrations, models
import proyectoferreteria.apps.gestionadmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0077_auto_20200325_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnoempleado',
            name='Id_Turno',
            field=models.AutoField(primary_key=True, serialize=False, validators=[proyectoferreteria.apps.gestionadmin.models.validartamaño]),
        ),
    ]
