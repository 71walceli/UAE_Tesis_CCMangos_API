from rest_framework import serializers
from django.db import transaction

from ..models import Lote
from .AreaSerializer import AreaSerializer


class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = "__all__"
        
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["Areas"] = [a.id for a in instance.Areas.filter(Activo = True)]
        return representation
