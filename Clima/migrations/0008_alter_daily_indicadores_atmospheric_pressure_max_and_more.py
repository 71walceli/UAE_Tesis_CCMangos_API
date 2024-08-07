# Generated by Django 4.2.1 on 2024-07-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clima', '0007_alter_daily_indicadores_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_indicadores',
            name='Atmospheric_Pressure_Max',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='daily_indicadores',
            name='Atmospheric_Pressure_Min',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
