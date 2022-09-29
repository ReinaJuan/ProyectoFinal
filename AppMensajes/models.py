from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    contenido = models.CharField(max_length=2000)
    emisor=models.ForeignKey(User, on_delete=models.CASCADE)
    receptor=models.CharField(max_length=2000)
    fecha=models.DateTimeField(null=True, auto_now_add=False, auto_now=False, blank=True)


    
