# Generated by Django 3.0.4 on 2020-03-26 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0087_auto_20200326_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facturadetalle',
            old_name='cantidad',
            new_name='Cantidad',
        ),
        migrations.RenameField(
            model_name='facturadetalle',
            old_name='idFacturaDetalle',
            new_name='Id_FacturaDetalle',
        ),
        migrations.RenameField(
            model_name='facturadetalle',
            old_name='idFacturaEncabezado',
            new_name='Id_Factura_Encabezado',
        ),
        migrations.RenameField(
            model_name='facturadetalle',
            old_name='idProducto',
            new_name='Id_Producto',
        ),
    ]
