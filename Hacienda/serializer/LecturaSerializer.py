from rest_framework import serializers
from Hacienda.models import Lectura
class LecturaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lectura
        fields = ('__all__')
        required_fields = ('SyncId', 'FechaVisita')
        extra_kwargs = {
            field: {'required': True}
            for field in required_fields
        }
    def validate(self, data):
        required = "es requerido"
        null = "no puede ser nulo"
        if not data:
            raise ValueError("Asegurese de enviar un formulario Válido!")
        if "Id_Planta" not in data or data.get("Id_Planta") is None:
            raise ValueError(f"Id_Planta: {required}")
        if "FechaVisita" not in data or data.get("FechaVisita") is None:
            raise ValueError(f"FechaVisita: {required}")
        if "SyncId" not in data or data.get("SyncId") is None: 
            raise ValueError(f"SyncId: {required}")
        return data
