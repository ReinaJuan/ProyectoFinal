from django import forms
from .models import *


class Formulariomensaje(forms.Form):
    contenido = forms.CharField(max_length=2000)
    receptor=forms.CharField(max_length=200)
    
    


    
