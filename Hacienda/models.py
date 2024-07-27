from datetime import datetime, timedelta
from enum import Enum
from django.db import models
import uuid
from django.contrib.auth.models  import User
from django.core.files.storage import FileSystemStorage  


class Hacienda(models.Model):
    codigo = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=40)
    Activo = models.BooleanField(default=True)
    Id_Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Proyecto(models.Model):
    # campo_fk = models.ForeignKey(ModeloPrincipal, on_delete=models.CASCADE, null=True)
    Id_Hacienda = models.ForeignKey(Hacienda, on_delete=models.CASCADE, null=True)
    Codigo_Proyecto = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=40)
    Densidad = models.IntegerField(null=True)
    Activo = models.BooleanField(default=True)
    Id_Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Variedad(models.Model):
    Codigo = models.CharField(max_length=5, blank=False, null=False)
    Nombre = models.CharField(max_length=30, blank=False, null=False)
    MaximaCosechaHectareaAnual = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    MinimaCosechaHectareaAnual = models.DecimalField(max_digits=8, decimal_places=2, null=False) 
    Activo = models.BooleanField(default=True)


# TODO Cambiar nombres de áreas y lotes
class Lote(models.Model):
    Id_Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True, related_name="Lotes")
    Codigo_Lote = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=40)
    Hectareas = models.DecimalField(max_digits=7, decimal_places=3, null=True)
    Activo = models.BooleanField(default=True)
    Id_Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Area(models.Model):
    Id_Lote = models.ForeignKey(Lote, on_delete=models.CASCADE, null=True, related_name="Areas")
    Codigo_Area = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=40, blank=True, null=True)
    Variedad = models.ForeignKey(Variedad, null=False, on_delete=models.CASCADE)
    Hectareas = models.DecimalField(max_digits=7, decimal_places=3, null=True)
    Activo = models.BooleanField(default=True)
    Id_Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Planta(models.Model):
    Id_Area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, related_name="Plantas")
    Codigo_Planta = models.CharField(max_length=20) 
    Nombre = models.CharField(max_length=40, blank=True, null=True)
    Circunferencia = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Activo = models.BooleanField(default=True)
    lat = models.DecimalField(max_digits=18, decimal_places=16, null=True)
    lng = models.DecimalField(max_digits=19, decimal_places=16, null=True)
    VisibleToStudent = models.BooleanField(null=False,default=True)


class PlantaFoto(models.Model):
    uri = models.FileField(storage=FileSystemStorage("/Uploads/Plantas/Fotos"))


class Poligono(models.Model):
    Id_Lote = models.ForeignKey(Lote, on_delete=models.CASCADE, null=True, related_name="Poligonos")
    Id_Area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, related_name="Poligonos")
    FillColor = models.CharField(max_length=7)
    Activo = models.BooleanField(default=True)
    Id_Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class GeoCoordenadas(models.Model):
    Id_Poligono = models.ForeignKey(Poligono, on_delete=models.CASCADE, null=True)
    lat = models.DecimalField(max_digits=18, decimal_places=16, null=False)
    lng = models.DecimalField(max_digits=19, decimal_places=16, null=False)
    Activo = models.BooleanField(default=True)
    Id_Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Enfermedad(models.Model):
    Codigo = models.CharField(max_length=5, blank=False, null=False)
    Nombre = models.CharField(max_length=30, blank=False, null=False)
    Activo = models.BooleanField(default=True)


class Lectura(models.Model):
    Id_Planta = models.ForeignKey(Planta, on_delete=models.CASCADE, null=True)
    
    CantidadInflorescencias = models.IntegerField(default=0, blank=False, null=False)
    CantidadFrutonIniciales = models.IntegerField(default=0, blank=False, null=False)
    CantidadFrutosMaduración = models.IntegerField(default=0, blank=False, null=False)
    CantidadInflorescenciasPerdidas = models.IntegerField(default=0, blank=False, null=False)
    Enfermedades = models.ManyToManyField(Enfermedad)
    Observacion = models.CharField(max_length=256, blank=True, null=True)
    
    FechaVisita = models.DateTimeField(null=True)
    Activo = models.BooleanField(default=True)
    Id_Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    GUIDLectura = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    SyncId = models.TextField(max_length=100, null=True)
    FechaRegistro = models.DateTimeField(auto_now_add=True)
    
    Coord_x = models.FloatField(blank=True, null=True)
    Coord_y = models.FloatField(blank=True, null=True)
    Coord_precision = models.FloatField(blank=True, null=True)


class Produccion(models.Model):
    Id_Area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    Id_Lote = models.ForeignKey(Lote, on_delete=models.CASCADE, null=True)
    Cantidad = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    Fecha = models.DateField(null=False)
    FechaRegistro = models.DateTimeField(auto_now_add=True)
    Activo = models.BooleanField(default=True)
    Id_Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
