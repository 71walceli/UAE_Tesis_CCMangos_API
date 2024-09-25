from rest_framework import serializers
from ..models import Area


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


    def validate(self, data):
        mutually_exclusive = ["Id_Area", "Id_Lote"]
        if (
            all(k in data for k in mutually_exclusive)
            or all(k not in data for k in mutually_exclusive)
        ):
            raise ValueError(f"Debe suplir {' o '.join(mutually_exclusive)}, al menos alguno.")
        return data
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["Codigo_Lote"] = f"{instance.Id_Lote.Codigo_Lote}"
        representation["Codigo"] = f"{representation['Codigo_Lote']}_{instance.Codigo_Area}"
        representation["NombreÁrea"] = instance.Id_Lote.Nombre
        representation["NombreCompleto"] = f"{representation['NombreÁrea']} - {instance.Nombre}"
        representation["Plantas"] = [a.id for a in instance.Plantas.filter(Activo = True)]
        return representation
