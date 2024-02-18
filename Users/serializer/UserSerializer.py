from django.contrib.auth.models import User
from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from Hacienda.models import Hacienda
from Users.models import Perfil
from rest_framework.exceptions import ErrorDetail
from django.db import transaction


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    def validar_cedula(self, cedula):
        # Verificar longitud de la cédula
        if len(cedula) != 10:
            raise ValidationError(["Cedula",[ErrorDetail(string="La longitud debe ser de 10 dígitos.")]])
        
        # Verificar que todos los caracteres sean dígitos
        if not cedula.isdigit():
            raise ValidationError(["Cedula",[ErrorDetail(string="Debe contener solo dígitos.")]])
        
        provincia = int(cedula[:2])
        if (provincia < 1 or provincia > 24) and provincia != 30:
            raise ValidationError(["Cedula",[ErrorDetail(string="La provincia no es válida.")]])
        # Obtener los primeros 9 dígitos
        digitos = list(map(int, cedula[:-1]))

        # Aplicar el algoritmo de Luhn
        for i in range(0, 9, 2):
            digitos[i] *= 2
            if digitos[i] > 9:
                digitos[i] -= 9

        suma_total = sum(digitos)
        digito_verificador = (10 - (suma_total % 10)) % 10

        # Comparar el dígito verificador calculado con el dígito verificador proporcionado
        return digito_verificador == int(cedula[-1])
    
    perfil = PerfilSerializer(required=False)
    class Meta:
        model = User
        fields = '__all__'#['username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    @transaction.atomic
    def create(self, validated_data):
        perfil_data = self.context.get('perfil_data') or validated_data
        print("perfil_data = ", perfil_data)
        if perfil_data is None:
            raise serializers.ValidationError(["Cedula",[ErrorDetail(string='La cedula es requerida')]])
        
        # Valida que el número de cédula sea único
        cedula = perfil_data.get('cedula')
        if not self.validar_cedula(cedula):
            print("El número de cédula es inválido!")
            raise ValidationError(["Cedula",[ErrorDetail(string='El número de cédula es inválido!')]])
        
        if User.objects.filter(perfil__cedula=cedula).exists():
            raise ValidationError(["Cedula",[ErrorDetail(string='El número de cédula ya está en uso!')]])
        print("Creando usuario...")
        user_data = {
            "email": perfil_data["email"],
            "first_name": perfil_data["first_name"],
            "last_name": perfil_data["last_name"],
            "username": perfil_data["username"],
            "password": perfil_data["password"],
        }
        user = User.objects.create_user(**user_data)
        print("Usuario creado:", user.username)
        
        perfil_data = {
            "cedula": perfil_data["cedula"],
            "Id_Hacienda": get_object_or_404(Hacienda, id=perfil_data["Id_Hacienda"]),
        }
        
        print("Creando perfil...")
        Perfil.objects.create(user=user, **perfil_data)
        print("Perfil creado:", Perfil.cedula)
        
        # Crea un perfil asociado a ese usuario
        return user

    @transaction.atomic
    def update(self, instance, validated_data):
        perfil_data = self.context.get('perfil_data') or validated_data
        print("perfil_data = ", perfil_data)
        if perfil_data is None:
            raise serializers.ValidationError(["Cedula",[ErrorDetail(string='La cedula es requerida')]])
        
        print("Actualizando usuario...")
        user_data = {
            "email": perfil_data.get("email", instance.email),
            "first_name": perfil_data.get("first_name", instance.first_name),
            "last_name": perfil_data.get("last_name", instance.last_name),
            "username": perfil_data.get("username", instance.username),
            "password": perfil_data.get("password", instance.password),
        }
        user_id = perfil_data["id"]
        user = User.objects.get(pk=user_id)
        for atributo, valor in user_data.items():
            setattr(user, atributo, valor)
        user.save()
        print("Usuario actualizado:", user.username)
        
        perfil_previo = Perfil.objects.get(user_id=user_id)
        cedula = perfil_data.get('cedula', perfil_previo.cedula)
        if not self.validar_cedula(cedula):
            print("El número de cédula es inválido!")
            raise ValidationError(["Cedula",[ErrorDetail(string='El número de cédula es inválido!')]])
        
        perfil_data = {
            "cedula": perfil_data.get("cedula", perfil_previo.cedula),
            "Id_Hacienda": get_object_or_404(Hacienda, id=perfil_data.get("Id_Hacienda", perfil_previo.Id_Hacienda)),
        }
        print("Actualizando perfil...")
        for atributo, valor in perfil_data.items():
            perfil_data[atributo] = valor
        perfil_previo.save()
        print("Perfil actualizado:", Perfil.cedula)
        
        # Crea un perfil asociado a ese usuario
        return user
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        perfil_data = representation.pop('perfil', None)
        if perfil_data is not None:
            for key, value in perfil_data.items():
                representation[key] = value
        return representation

