# Generated by Django 4.2.1 on 2024-07-31 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hacienda', '0069_alter_area_poligono_alter_lote_poligono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planta',
            name='VisibleToStudent',
        ),
        migrations.AddField(
            model_name='planta',
            name='Altitud',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
