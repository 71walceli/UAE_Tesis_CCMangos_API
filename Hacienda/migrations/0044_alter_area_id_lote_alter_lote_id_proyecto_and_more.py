# Generated by Django 4.2.1 on 2024-01-14 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hacienda', '0043_alter_planta_id_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='Id_Lote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Areas', to='Hacienda.lote'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='Id_Proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Lotes', to='Hacienda.proyecto'),
        ),
        migrations.AlterField(
            model_name='planta',
            name='Id_Area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Plantas', to='Hacienda.area'),
        ),
    ]