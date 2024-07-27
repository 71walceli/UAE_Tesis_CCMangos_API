from rest_framework import serializers
from ..models import GeoCoordenadas


class GeoCoordenadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoCoordenadas
        fields = ('__all__')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['lat'] = float(representation['lat'])
        representation['lng'] = float(representation['lng'])
        return representation
