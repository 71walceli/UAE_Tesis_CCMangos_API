# Generated by Django 4.2.1 on 2024-01-14 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hacienda', '0040_remove_planta_id_lote_area_planta_id_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='poligono',
            name='Id_Area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hacienda.area'),
        ),
    ]
