from django.shortcuts import render
from AppsProyecto.forms import Usuarioform,Noticiasform
from AppsProyecto.models import Usuario,Noticias
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
            return render (request, "AppsProyecto/inicio.html", {"mensaje": "Error"})
 else:
    form= Usuarioform()
    return render(request, "AppsProyecto/usuario.html", {"formulario":form})


    #-----------------------------------------------------------------------------

def notis(request):

 if request.method=="POST":
        form = Noticiasform(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            tiponoticia= info["tiponoticia"]
            noticias= Noticias(tiponoticia=tiponoticia)
            noticias.save()
            return render (request, "AppsProyecto/noticias.html", {"mensaje": "Noticia creada"})
        
 else:
    form= Noticiasform()
    return render(request, "AppsProyecto/noticias.html", {"formulario":form})

def deportes(request):
    return render (request, "AppsProyecto/deportes.html")

def espectaculo(request):
    return render (request, "AppsProyecto/espectaculo.html")

def clima(request):
    return render (request, "AppsProyecto/clima.html")

def inicio(request):
    return render (request, "AppsProyecto/inicio.html")




