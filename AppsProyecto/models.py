from django.db import models
from datetime import date

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

class Noticias(models.Model):
      tiponoticia = models.CharField(max_length=50)
      ubicacion = models.CharField(max_length=50)
      fecha = models.DateField(blank=True, null=True, default=date.today())

class Deportes(models.Model):
      tipodeporte = models.CharField(max_length=50)
      ubicacion = models.CharField(max_length=50)
      fecha = models.DateField(blank=True, null=True, default=date.today())




      



