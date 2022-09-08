from django import forms 
from .models import *



class Usuarioform(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()

class Noticiasform(forms.Form):
    tiponoticia = forms.CharField(max_length=50)
    
