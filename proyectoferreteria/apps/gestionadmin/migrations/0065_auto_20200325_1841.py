# Generated by Django 3.0.4 on 2020-03-26 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0064_auto_20200325_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='garantia',
            old_name='descripcionGarantia',
            new_name='Descripcion_Garantia',
        ),
        migrations.RenameField(
            model_name='garantia',
            old_name='idGarantia',
            new_name='Id_Garantia',
        ),
        migrations.RenameField(
            model_name='garantia',
            old_name='tiempoGarantiaMes',
            new_name='Tiempo_Garantia_Mes',
        ),
        migrations.RenameField(
            model_name='proveedor',
            old_name='idProveedor',
            new_name='IdProveedor',
        ),
    ]
