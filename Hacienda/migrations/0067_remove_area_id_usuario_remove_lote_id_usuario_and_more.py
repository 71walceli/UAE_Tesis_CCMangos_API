# Generated by Django 4.2.1 on 2024-07-27 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hacienda', '0066_remove_geocoordenadas_id_usuario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='Id_Usuario',
        ),
        migrations.RemoveField(
            model_name='lote',
            name='Id_Usuario',
        ),
        migrations.AlterField(
            model_name='area',
            name='Poligono',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hacienda.poligono'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='Poligono',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hacienda.poligono'),
        ),
    ]
