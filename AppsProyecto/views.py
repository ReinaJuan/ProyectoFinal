from django.shortcuts import render
from AppsProyecto.forms import Usuarioform
from AppsProyecto.models import Usuario
from django.http import HttpResponse




# Create your views here.
def users(request):

 if request.method=="POST":
        form = Usuarioform(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            email= info["email"]
            usuario= Usuario(nombre=nombre, apellido=apellido, email=email)
            usuario.save()
            return render (request, "AppsProyecto/usuario.html", {"mensaje": "Usuario Creado"})
        else:
            return render (request, "AppsProyecto/usuario.html", {"mensaje": "Registrate para ingresar"})
 else:
    form= Usuarioform()
    return render(request, "AppsProyecto/usuario.html", {"formulario":form})
