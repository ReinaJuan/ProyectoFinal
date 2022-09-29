from django.shortcuts import render
import datetime
from AppMensajes.models import *
from AppMensajes.forms import *
from django.contrib.auth.decorators import login_required

@login_required 
def mensaje(request):
    if (request.method == "POST"):
        form = Formulariomensaje(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            receptor_info = info.get("receptor")
            receptor = User.objects.filter(username = receptor_info)
            if (len(receptor) == 0):
                return (render(request, "AppsProyecto/inicio.html", {"mensajito": "Usuario receptor no encontrado"}))
            else:
                emisor = request.user
                contenido = info.get("contenido")
                fecha = datetime.datetime.today()
                mensaje = Mensaje(contenido = contenido, emisor = emisor, receptor = receptor_info,fecha = fecha)
                mensaje.save()
                return (render(request, "AppsProyecto/inicio.html", {"mensajito": "Mensaje Enviado"}))
        else:
            return (render(request, "AppsProyecto/inicio.html", {"mensajito": "Formulario no válido"}))
    else:
        form = Formulariomensaje()
    return (render(request, "AppMensajes/mensaje.html", {"formulario": form}))

@login_required    
def bandejaaentrada(request):
        mensajes = Mensaje.objects.filter(receptor = request.user.username)
        if (len(mensajes) != 0):
            return render(request, "AppMensajes/bandejaentrada.html", {"aviso": "Viendo todos los mensajes recibidos", "mensajes": mensajes})
        else:
            return render(request, "AppMensajes/bandejaentrada.html", {"aviso": "No tienes mensajes"})

@login_required    
def bandejasalida(request):
        mensajes = Mensaje.objects.filter(emisor = request.user)
        if (len(mensajes) != 0):
            return render(request, "AppMensajes/bandejasalida.html", {"aviso": "Viendo todos los mensajes enviados", "mensajes": mensajes})
        else:
            return render(request, "AppMensajes/bandejasalida.html", {"aviso": "No enviaste ningún mensaje"})
    
def mensajes(request):
    return (render(request, "AppMensajes/mensaje.html"))
