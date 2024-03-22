from rest_framework import serializers
from Hacienda.models import Lote,Produccion
import locale
class ProduccionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Produccion
        fields = ('__all__')
    def validate(self, data):
        mutually_exclusive = ["Id_Area", "Id_Lote"]
        if (
            all(k in data for k in mutually_exclusive)
            or all(k not in data for k in mutually_exclusive)
        ):
            raise ValueError(f"Debe suplir {' o '.join(mutually_exclusive)}, al menos alguno.")
        return data
