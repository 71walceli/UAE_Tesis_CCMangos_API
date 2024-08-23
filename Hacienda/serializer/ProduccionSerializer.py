from rest_framework import serializers

from Hacienda.models import Lote,Produccion
from .VariedadSerializer import VariedadSerializer


class ProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produccion
        fields = ('__all__')
    
    
    def validate(self, data):
        mutually_exclusive = ["Id_Area", "Id_Lote"]
        for key in mutually_exclusive:
            if key in data and data[key] is None:
                del data[key]
        if (
            all(k in data for k in mutually_exclusive)
            or all(k not in data for k in mutually_exclusive)
        ):
            raise ValueError(f"Debe suplir {' o '.join(mutually_exclusive)}, al menos alguno.")
        return data


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["Variedad"] = VariedadSerializer(instance.Id_Area.Variedad).data
        return representation
