# Generated by Django 4.2.1 on 2024-01-14 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Hacienda", "0042_alter_planta_id_area"),
    ]

    operations = [
        migrations.AlterField(
            model_name="planta",
            name="Id_Area",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="areas",
                to="Hacienda.area",
            ),
        ),
    ]
