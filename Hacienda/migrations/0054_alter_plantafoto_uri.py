# Generated by Django 4.2.1 on 2024-04-10 11:11

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Hacienda", "0053_alter_plantafoto_uri"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plantafoto",
            name="uri",
            field=models.FileField(
                storage=django.core.files.storage.FileSystemStorage(
                    "Uploads/Plantas/Fotos"
                ),
                upload_to="",
            ),
        ),
    ]
