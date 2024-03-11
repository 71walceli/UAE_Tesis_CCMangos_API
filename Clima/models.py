from pyexpat import model
from django.db import models

# Create your models here.
class Daily_Indicadores(models.Model):
    #Date info
    Date = models.DateTimeField(blank=True, null=True)
    Date_Arable_Sync = models.DateTimeField(blank=True, null=True)
    Date_Sync = models.DateTimeField(auto_created=True,blank=True, null=True)
    #Location Info
    Lat = models.DecimalField(max_digits=18, decimal_places=16, null=True)
    Lng = models.DecimalField(max_digits=18, decimal_places=16, null=True)
    LocationID = models.CharField(null=True)
    #device
    Device = models.CharField(null=True)
    #Precipitation
    Precipitation = models.DecimalField(max_digits=18, decimal_places=16, null=True)
    
    #Temp Air
    Temp_Air_Mean = models.DecimalField(max_digits=5, decimal_places=2,null= True)
    Temp_Air_Min = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    Temp_Air_Max = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    
    #Dew Temp
    Dew_Temp_Mean = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    Dew_Temp_Max = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    Dew_Temp_Min = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    
    # Relative Humidity
    Relat_Hum_Mean = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    Relat_Hum_Min = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    Relat_Hum_Max = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    
    # Wind Speed in mps
    Wind_Speed_Mean = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    Wind_Speed_Min = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    Wind_Speed_Max = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    
    #Sea Level Pressure
    Atmospheric_Pressure_Max = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    Atmospheric_Pressure_Min = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    
    Activo = models.BooleanField(default=True)
    Usuario = models.TextField(default="Arable",max_length=100, null=True)

