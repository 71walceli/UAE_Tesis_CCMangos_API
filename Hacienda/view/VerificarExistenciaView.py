from Hacienda.models import Produccion
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Hacienda.serializers import ProduccionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .CrudApiView import CrudApiView
import Hacienda.models as models
import Hacienda.serializers as serializers


class VerificarExistenciaAPIView(APIView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def __init__(self):
        super()

    def get(self, request, *args, **kwargs):
        try:
            entidad = request.GET["entidad"]
            codigo = request.GET["codigo"]
            
            entidad = entidad[0].upper() + entidad[1:].lower()
            Entidad = getattr(models, entidad)
            Serializer = getattr(serializers, f"{entidad}Serializer")
        except KeyError:
            response = {
                "message": "Faltan datos por enviar"
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            response = {
                "message": "Entidad no encontrada"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
        filters = {
            f"Codigo_{entidad}": codigo,
            "Activo": True,
        }
        objects = Entidad.objects.filter(**filters)
        found = objects.exists()
        response = {
            "result": found,
            "objects": Serializer(objects,many=True).data,
        }
        return Response(response)
