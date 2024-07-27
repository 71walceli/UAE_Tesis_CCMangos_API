from rest_framework import serializers
from Hacienda.models import Variedad


class VariedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variedad
        fields = ('__all__')
        required_fields = ('SyncId', 'FechaVisita')
        extra_kwargs = {
            field: {'required': True}
            for field in required_fields
        }
