from rest_framework import serializers
from ..models import Proyecto
class ProyectoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('__all__')
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["Lotes"] = [a.id for a in instance.Lotes.all() if a.Activo]
        return representation
