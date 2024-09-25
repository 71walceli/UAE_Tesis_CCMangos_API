from rest_framework import serializers
from datetime import datetime, timedelta

from Hacienda.models import Planta,Lectura


class PlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planta
        fields = ('__all__')
        required_fields = ('Codigo_Planta', 'Nombre')
        extra_kwargs = {
            field: {'required': True}
            for field in required_fields
        }
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["Disabled"] = False
        representation["Codigo_Area"] = f"{instance.Id_Area.Id_Lote.Codigo_Lote}_{instance.Id_Area.Codigo_Area}"
        representation["Codigo"] = f"{representation['Codigo_Area']}_{instance.Codigo_Planta}" 
        representation["NombreLote"] = f"{instance.Id_Area.Id_Lote.Nombre} - {instance.Id_Area.Nombre}"
        representation["NombreCompleto"] = f"{representation['NombreLote']} - {instance.Nombre or instance.Codigo_Planta}"
        return representation
