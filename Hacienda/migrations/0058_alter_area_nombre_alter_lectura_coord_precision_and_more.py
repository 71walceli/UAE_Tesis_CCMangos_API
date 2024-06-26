# Generated by Django 4.2.1 on 2024-05-29 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hacienda', '0057_alter_area_nombre_alter_lectura_coord_precision_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='Nombre',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='lectura',
            name='Coord_precision',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lectura',
            name='Coord_x',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lectura',
            name='Coord_y',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='planta',
            name='Nombre',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
