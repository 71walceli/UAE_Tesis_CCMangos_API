from Users.models import Perfil
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from Users.serializer.UserSerializer import UserSerializer

"""Document by SWAGGER"""
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UsuarioList(APIView):
    def get(self, request, format=None):
        rol = request.query_params.get('rol', None)
        if rol:
            usuarios = User.objects.filter(groups__name=rol)
        else:
            usuarios = User.objects.filter(is_active=True)
        serializer = UserSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        user_data = {
            "cedula": request.data.get("cedula"),
            "email": request.data.get("email"),
            "first_name": request.data.get("first_name"),
            "last_name": request.data.get("last_name"),
            "username": request.data.get("username"),
            "password": request.data.get("username"),
            "Id_Hacienda": request.data.get("Id_Hacienda"),
            **request.data,
        }
        if None in user_data.values():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.create(user_data)
            return Response(status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        user_data = {
            "id": request.data.get("id"),
            **request.data,
        }
        if user_data["id"] is None:
            print("request =", request.data)
            print("id =", user_data["id"])
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        usuario_previo = User.objects.get(pk=user_data["id"])
        
        user_serializer = UserSerializer(usuario_previo, data=user_data, partial=True) 
        if user_serializer.is_valid():
            user_serializer.save(**request.data)
            return Response(status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = request.GET.get("id")
        if not id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        usuario_previo = User.objects.get(pk=id)
        if not usuario_previo:
            return Response(status=status.HTTP_404_NOT_FOUND)
        usuario_previo.is_active = False
        usuario_previo.save()
        return Response(status=status.HTTP_200_OK)
