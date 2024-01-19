from rest_framework import serializers
from ..models import Lote
from .PoligonoSerializer import PoligonoSerializers
from .AreaSerializer import AreaSerializer
class LoteSerializers(serializers.ModelSerializer):
    poligonos = PoligonoSerializers(many=True, read_only=True)
    class Meta:
        model = Lote
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["Areas"] = [a.id for a in instance.Areas.filter(Activo = True)]
        representation["Poligonos"] = [a.id for a in instance.Poligonos.filter(Activo = True)]
        return representation
