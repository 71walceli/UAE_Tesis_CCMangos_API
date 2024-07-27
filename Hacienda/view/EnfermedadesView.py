from Hacienda.models import Enfermedad
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Hacienda.serializers import EnfermedadSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .CrudApiView import CrudApiView


class EnfermedadAPIView(CrudApiView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def __init__(self):
        super().__init__(Enfermedad, EnfermedadSerializer)
    
    def get(self, request, *args, **kwargs):
        id_lotes = self.kwargs.get('id_lotes')
        if id_lotes: 
            kwargs["filters"] = dict(ID_Lote=id_lotes)
        return super().get(self, request, *args, **kwargs)
