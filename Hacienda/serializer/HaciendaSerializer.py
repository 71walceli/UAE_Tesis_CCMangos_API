from rest_framework import serializers
from ..models import Hacienda


class HaciendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hacienda
        fields = ('__all__')
