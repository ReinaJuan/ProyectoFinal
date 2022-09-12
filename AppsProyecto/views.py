from django.shortcuts import render
from AppsProyecto.forms import Usuarioform,Noticiasform,Deportesform
from AppsProyecto.models import Usuario,Noticias,Deportes
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
            ubicacion= info["ubicacion"]
            fecha= info["fecha"]
            
            noticias= Noticias(tiponoticia=tiponoticia, ubicacion=ubicacion,fecha=fecha)
            noticias.save()
            return render (request, "AppsProyecto/noticias.html", {"mensaje": "Noticia creada"})
        else:
            return render (request, "AppsProyecto/noticias.html", {"mensaje": "Error"})
        
 else:
    form= Noticiasform()
    return render(request, "AppsProyecto/noticias.html", {"formulario":form})

#----------------------------------------------------------------------------------------------
def deportes(request):

 if request.method=="POST":
        form = Deportesform(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            tipodeporte= info["tipodeporte"]
            ubicacion= info["ubicacion"]
            fecha= info["fecha"]
            deportes= Deportes(tipodeporte=tipodeporte, ubicacion=ubicacion, fecha=fecha)
            deportes.save()
            return render (request, "AppsProyecto/deportes.html", {"mensaje": "Deporte creado"})
        else:
            return render (request, "AppsProyecto/deportes.html", {"mensaje": "Error"})
        
 else:
    form= Deportesform()
    return render(request, "AppsProyecto/deportes.html", {"formulario":form})

#----------------------------------------------------------------------------------------------------
def busquedausuario(request):
    return render(request, "AppsProyecto/busquedausuario.html")

def buscar(request):
    if request.GET["apellido"]:
        surname=request.GET["apellido"]
        usuario=Usuario.objects.filter(apellido=surname)
        if len(usuario)!=0:
            return render(request, "AppsProyecto/resultadousuario.html", {"usuario":usuario})
        else:
            return render(request, "AppsProyecto/resultadousuario.html", {"mensaje": "No se encuentra usuario"})
    else:
        return render(request, "AppsProyecto/busquedausuario.html", {"mensaje": "No enviaste datos"})











def espectaculo(request):
    return render (request, "AppsProyecto/espectaculo.html")

def clima(request):
    return render (request, "AppsProyecto/clima.html")

def inicio(request):
    return render (request, "AppsProyecto/inicio.html")




