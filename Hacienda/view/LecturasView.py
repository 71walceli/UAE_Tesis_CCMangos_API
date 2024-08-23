from Hacienda.models import Lectura
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Hacienda.serializers import LecturaSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
#http
from django.http import Http404

from .CrudApiView import CrudApiView


class LecturaAPIView(CrudApiView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def __init__(self):
        parents = [
            "Id_Planta_id",
            "Id_Area_id",
            "Id_Lote_id",
            "Id_Proyecto_id",
            "Id_Hacienda_id",
        ]
        super().__init__(Lectura, LecturaSerializer, parents)
   