from Hacienda.models import Lectura
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Hacienda.serializers import LecturaSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
#http
from django.http import Http404
#Import custom validators


class LecturaAPIView(APIView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # Código existente...
    def get(self, request):
    
        id = self.kwargs.get('id')
      
        if id:
            lecturas = Lectura.objects.filter(Id_Lectura = id)
            serializer = LecturaSerializers(lecturas, many=True)
            return Response(serializer.data)

        lecturas = Lectura.objects.all()
        serializer = LecturaSerializers(lecturas, many=True)
        return Response(serializer.data)
    def post(self, request):
        user = request.user
        print(request.data)
        #validate = ValidateLectura(request.data)
        #if validate != "":
        #    return Response(validate, status=status.HTTP_400_BAD_REQUEST)
        user = request.user
        username = user.username
        request.data["Usuario"] = username
        # Validar que solo exista una lectura por mes de una Id_Planta
        fecha_visita = request.data.get("FechaVisita")
        id_planta = request.data.get("Id_Planta")
        # Convertir fecha_visita a datetime si es una cadena
        if isinstance(fecha_visita, str):
            try:
                fecha_visita = datetime.strptime(fecha_visita, "%Y-%m-%dT%H:%M:%S.%fZ")
            except ValueError as e:
                return Response(f"Error al analizar la fecha: {str(e)}", status=status.HTTP_400_BAD_REQUEST)
        
        lecturas_mes = Lectura.objects.filter(FechaVisita__month=datetime.now().month, FechaVisita__year=datetime.now().year, Id_Planta=id_planta)
        if lecturas_mes.exists():
            print(f"{id_planta} ya tiene una lectura")
            return Response("Ya existe una lectura de esta planta en este mes!", status=status.HTTP_400_BAD_REQUEST)
        # Crear un serializador para los datos de la solicitud
        serializer = LecturaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(f"{username} Ha registrado una lectura")
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Lectura.objects.get(pk=pk)
        except Lectura.DoesNotExist:
            raise Http404

    def delete (self, request, id):
        lectura = self.get_object(id)
        lectura.Activo = False
        lectura.save()

        serializer = LecturaSerializers(lectura)
        return Response(serializer.data)