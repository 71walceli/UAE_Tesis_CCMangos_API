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


class LecturaAPIView(APIView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        id = self.kwargs.get('id')
        if id:
            lecturas = Lectura.objects.filter(Id_Lectura = id)
            serializer = LecturaSerializer(lecturas, many=True)
            return Response(serializer.data)
        lecturas = Lectura.objects.filter(Activo = True)
        serializer = LecturaSerializer(lecturas, many=True)
        return Response(serializer.data)
    def post(self, request):
        user = request.user
        print(request.data)
        user = request.user
        username = user.username
        request.data["Usuario"] = username
        
        serializer = LecturaSerializer(data=request.data)
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

    def delete (self, request):
        id = request.GET.get("id", 0)
        lectura = self.get_object(id)
        lectura.Activo = False
        lectura.save()

        serializer = LecturaSerializer(lectura)
        return Response(serializer.data)