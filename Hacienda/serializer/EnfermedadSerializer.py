from rest_framework import serializers
from Hacienda.models import Enfermedad
class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedad
        fields = ('__all__')
        required_fields = ('SyncId', 'FechaVisita')
        extra_kwargs = {
            field: {'required': True}
            for field in required_fields
        }
