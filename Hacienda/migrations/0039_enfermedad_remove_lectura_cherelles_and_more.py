# Generated by Django 4.2.1 on 2023-12-31 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hacienda', '0038_rename_visible_planta_visibletostudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=5)),
                ('Nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='lectura',
            name='Cherelles',
        ),
        migrations.RemoveField(
            model_name='lectura',
            name='E1',
        ),
        migrations.RemoveField(
            model_name='lectura',
            name='E2',
        ),
        migrations.RemoveField(
            model_name='lectura',
            name='E3',
        ),
        migrations.RemoveField(
            model_name='lectura',
            name='E4',
        ),
        migrations.RemoveField(
            model_name='lectura',
            name='E5',
        ),
        migrations.RemoveField(
            model_name='lectura',
            name='GR1',
        ),
        migrations.RemoveField(
            model_name='lectura',
            name='GR2',
        ),
        migrations.RemoveField(
            model_name='lectura',
            name='GR3',
        ),
        migrations.RemoveField(
            model_name='lectura',
            name='GR4',
        ),
        migrations.RemoveField(
            model_name='lectura',
            name='GR5',
        ),
        migrations.RemoveField(
            model_name='lectura',
            name='Monilla',
        ),
        migrations.RemoveField(
            model_name='lectura',
            name='Total',
        ),
        migrations.AddField(
            model_name='lectura',
            name='CantidadFrutonIniciales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lectura',
            name='CantidadFrutosMaduración',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lectura',
            name='CantidadInflorescencias',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lectura',
            name='CantidadInflorescenciasPerdidas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lectura',
            name='Observacion',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='planta',
            name='Id_Lote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hacienda.lote'),
        ),
        migrations.AddField(
            model_name='lectura',
            name='Enfermedades',
            field=models.ManyToManyField(to='Hacienda.enfermedad'),
        ),
    ]
