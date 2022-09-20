from django.db import models
from datetime import date
from ckeditor.fields import RichTextField

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

class Tag (models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="post", default="placeholder.png")
    state = models.BooleanField('Active',default=False)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
	    return self.title




      



