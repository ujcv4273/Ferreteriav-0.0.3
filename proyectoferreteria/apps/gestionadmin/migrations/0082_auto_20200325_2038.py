# Generated by Django 3.0.4 on 2020-03-26 02:38

from django.db import migrations, models
import proyectoferreteria.apps.gestionadmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0081_auto_20200325_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='Id_Empleado',
            field=models.AutoField(primary_key=True, serialize=False, validators=[proyectoferreteria.apps.gestionadmin.models.validartamaño]),
        ),
    ]
