from django.shortcuts import render,redirect
from AppsProyecto.forms import *
from AppsProyecto.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm





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
    posts = Post.objects.filter(state=True)
    form = PostForm(request.POST, request.FILES)
    context = {'form':form,'posts':posts}
    return render (request, 'AppsProyecto/inicio.html',context)
#------------------------------------------------------------------------------------
@login_required
def insertPost(request):
    posts = Post.objects.filter(state=True)

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'AppsProyecto/inicio.html',{"mensaje": "Publicacion creada"})   
    context = {'form':form,'posts':posts}
    return render (request, 'AppsProyecto/publicar.html',context)
    


def post(request, pk):
	post = Post.objects.get(id=pk)
	context = {'post':post}
	return render(request, 'AppsProyecto/post.html', context)

@login_required 
def editPost(request, pk):
    post =  Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return render(request, 'AppsProyecto/inicio.html')    
    context = {'form':form}
    return render (request, 'AppsProyecto/publicar.html',context)
#--------------------------------------------------------------------------------------------
def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST )
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'AppsProyecto/inicio.html', {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, 'AppsProyecto/login.html', {"form":form, 'mensaje':'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'AppsProyecto/login.html', {"form":form, 'mensaje':'Usuario o contraseña incorrectos'})
    else:
        form=AuthenticationForm()
        return render(request, 'AppsProyecto/login.html', {'form':form})


def register(request):
    if request.method=="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            

            form.save()
            return render(request, 'AppsProyecto/inicio.html', {'mensaje':f"Usuario {username} creado"})
    else:
        form=UserRegisterForm()
    return render(request, 'AppsProyecto/register.html', {'form':form})

        
@login_required        
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form= UserEditForm(request.POST)
        if form.is_valid():
            usuario.first_name=form.cleaned_data["first_name"]
            usuario.last_name=form.cleaned_data["last_name"]
            usuario.email=form.cleaned_data["email"]
            usuario.password1=form.cleaned_data["password1"]
            usuario.password2=form.cleaned_data["password2"]
            usuario.save()
            return render(request, 'AppsProyecto/inicio.html', {'mensaje':f"Perfil de {usuario} editado"})
    else:
        form= UserEditForm(instance=usuario)
    return render(request, 'AppCoder/editarPerfil.html', {'form':form, 'usuario':usuario})




