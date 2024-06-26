# Generated by Django 4.2.1 on 2024-03-10 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Clima", "0002_daily_indicadores_delete_indicadores"),
    ]

    operations = [
        migrations.RenameField(
            model_name="daily_indicadores",
            old_name="Crop_Water_Demand",
            new_name="Atmospheric_Pressure_Max",
        ),
        migrations.RenameField(
            model_name="daily_indicadores",
            old_name="Dli",
            new_name="Atmospheric_Pressure_Min",
        ),
        migrations.RenameField(
            model_name="daily_indicadores",
            old_name="Evapotranspiration",
            new_name="Wind_Speed_Max",
        ),
        migrations.RenameField(
            model_name="daily_indicadores",
            old_name="Evapotranspiration_Crop",
            new_name="Wind_Speed_Mean",
        ),
        migrations.RenameField(
            model_name="daily_indicadores",
            old_name="Ndvi",
            new_name="Wind_Speed_Min",
        ),
        migrations.RemoveField(
            model_name="daily_indicadores",
            name="Relat_Hum_Max_Temp",
        ),
        migrations.RemoveField(
            model_name="daily_indicadores",
            name="Relat_Hum_Min_Temp",
        ),
        migrations.RemoveField(
            model_name="daily_indicadores",
            name="Sea_Level_Pressure",
        ),
        migrations.RemoveField(
            model_name="daily_indicadores",
            name="Shortwave_Downwelling",
        ),
        migrations.RemoveField(
            model_name="daily_indicadores",
            name="Temp_Air_Max_Day",
        ),
        migrations.RemoveField(
            model_name="daily_indicadores",
            name="Temp_Air_Min_Day",
        ),
        migrations.RemoveField(
            model_name="daily_indicadores",
            name="Temp_Below",
        ),
        migrations.RemoveField(
            model_name="daily_indicadores",
            name="Temp_Below_Mean",
        ),
        migrations.RemoveField(
            model_name="daily_indicadores",
            name="Vapor_Pressure",
        ),
        migrations.RemoveField(
            model_name="daily_indicadores",
            name="Vapor_Pressure_Deficit",
        ),
    ]
