from Hacienda.models import Area
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Hacienda.serializers import AreaSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .CrudApiView import CrudApiView


class AreaAPIView(CrudApiView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def __init__(self):
        parents = [
            "Id_Lote_id",
            "Id_Proyecto_id",
            "Id_Hacienda_id",
        ]
        super().__init__(Area, AreaSerializer, parents)
    
    def get(self, request, *args, **kwargs):
        id_lotes = self.kwargs.get('id_lotes')
        if id_lotes: 
            kwargs["filters"] = dict(ID_Lote=id_lotes)
        return super().get(self, request, *args, **kwargs)
    