from Hacienda.models import Planta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Hacienda.serializers import PlantaSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class PlantaAPIView(APIView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request,*args, **kwargs):
        user = request.user
        grupos_usuario = user.groups.all()
        id_area = request.GET.get('id_area')
        if id_area: 
            plantas = Planta.objects.filter(Id_Area = id_area, Activo=True)
            serializer = PlantaSerializers(plantas, many=True)
        if any(grupo.name == "Estudiante" for grupo in grupos_usuario):
            plantas = Planta.objects.filter(Activo=True, Visible=True)
            serializer = PlantaSerializers(plantas, many=True)
        if any(grupo.name == "Tecnico" for grupo in grupos_usuario):
            plantas = Planta.objects.filter(Activo=True, Visible=True)
            serializer = PlantaSerializers(plantas, many=False)
        else:
            plantas = Planta.objects.filter(Activo=True)
            serializer = PlantaSerializers(plantas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlantaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, *args, **kwargs):
        id = request.data.get("id")
        if not id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        planta = self.get_object(id)
        if not planta:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PlantaSerializers(planta, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # TODO Unduplicate. Might need to superclass views like this.
    def get_object(self, pk):
        try:
            return Planta.objects.get(pk=pk)
        except Planta.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def delete (self, request, *args, **kwargs):
        id = request.GET.get("id")
        if not id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        planta = self.get_object(id)
        if not planta:
            return Response(status=status.HTTP_404_NOT_FOUND)
        planta.Activo = False
        planta.save()

        serializer = PlantaSerializers(planta)
        return Response(serializer.data)
