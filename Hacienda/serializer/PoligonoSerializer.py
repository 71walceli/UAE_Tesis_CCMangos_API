from rest_framework import serializers
from ..models import Poligono
from .GeoCoordenadasSerializer import GeoCoordenadasSerializer


class PoligonoSerializer(serializers.ModelSerializer):
    coordenadas = GeoCoordenadasSerializer(many=True, read_only=True) 
    class Meta:
        model = Poligono
        fields = '__all__'
