from django import forms 
from .models import *
from datetime import date




class Usuarioform(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()

class Noticiasform(forms.Form):
      tiponoticia = forms.CharField(max_length=500)
      ubicacion = forms.CharField(max_length=500)
      fecha = forms.DateField( )

class Deportesform(forms.Form):
      tipodeporte=forms.CharField(max_length=50)
      ubicacion=forms.CharField(max_length=50)
      fecha = forms.DateField( )
    
