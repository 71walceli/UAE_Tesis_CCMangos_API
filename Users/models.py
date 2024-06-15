"""Users models"""
from django.contrib.auth.models  import User, Group
from django.db import models

from Hacienda.models import Hacienda
# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=10) 
    created = models.DateField(auto_now=True)
    # TODO Cambiar a modified
    modifief = models.DateField(auto_now=True)
    Id_Hacienda = models.ForeignKey(Hacienda, on_delete=models.CASCADE, null=True)

    roles = models.ManyToManyField(Group)

    def __str__(self):
        return self.user.username
