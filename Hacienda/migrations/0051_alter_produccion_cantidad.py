# Generated by Django 4.2.1 on 2024-03-22 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hacienda', '0050_alter_produccion_id_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='Cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
