from Hacienda.models import Lote, Area
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Hacienda.serializers import LoteSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .CrudApiView import CrudApiView


class LoteAPIView(CrudApiView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def __init__(self):
        super().__init__(Lote, LoteSerializers)

    def get(self, request, *args, **kwargs):
        id_proyecto = request.GET.get('id_proyecto')
        if id_proyecto: 
            kwargs["filters"] = dict(Id_Proyecto=id_proyecto)
        return super().get(self, request, *args, **kwargs)
