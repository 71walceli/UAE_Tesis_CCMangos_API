# Generated by Django 4.2.1 on 2024-03-10 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Clima", "0004_remove_daily_indicadores_sunshine_duration"),
    ]

    operations = [
        migrations.RenameField(
            model_name="daily_indicadores",
            old_name="Dew_Temp_At_Min_Temp",
            new_name="Dew_Temp_Min",
        ),
    ]