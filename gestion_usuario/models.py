from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Para aplicar imagefiel necesitamos instalar Pillows -> pip install Pillow
    foto_perfil = models.ImageField(upload_to='foto_perfil', blank=True)
    def __str__(self):
        return self.user.username




class Producto(models.Model):
    nombreproducto = models.CharField(max_length=100)
    costopresupuestado = models.IntegerField()
    precioproducto = models.IntegerField()
    tienda = models.CharField(max_length=100)
    nota = models.CharField(max_length=200)

    
    