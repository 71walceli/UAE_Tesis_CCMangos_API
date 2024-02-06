from Hacienda.models import Planta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Hacienda.serializers import PlantaSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .CrudApiView import CrudApiView


class PlantaAPIView(CrudApiView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def __init__(self):
        super().__init__(Planta, PlantaSerializers)
    
    def get(self, request, *args, **kwargs):
        grupos_usuario = request.user.groups.all()
        id_area = request.GET.get('id_area')
        if id_area: 
            kwargs["filters"] = dict(Id_Area=id_area)
        if any(grupo.name == "Estudiante" for grupo in grupos_usuario):
            kwargs["filters"] = dict(Visible=True)
        if any(grupo.name == "Tecnico" for grupo in grupos_usuario):
            kwargs["filters"] = dict(Visible=True)
            kwargs["many"] = False
        return super().get(self, request, *args, **kwargs)
