from datetime import datetime
from django.shortcuts import render,redirect
from AppsProyecto.forms import *
from AppsProyecto.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.




#----------------------------------------------------------------------------------------------------
def busquedausuario(request):
    return render(request, "AppsProyecto/busquedausuario.html")

def buscar(request):
    if request.GET["apellido"]:
        surname=request.GET["apellido"]
        usuario=User.objects.filter(apellido=surname)
        if len(usuario)!=0:
            return render(request, "AppsProyecto/resultadousuario.html", {"usuario":usuario})
        else:
            return render(request, "AppsProyecto/resultadousuario.html", {"mensaje": "No se encuentra usuario"})
    else:
        return render(request, "AppsProyecto/busquedausuario.html", {"mensaje": "No enviaste datos"})


def inicio(request):
    posts = Post.objects.filter(state=True)
    form = PostForm(request.POST, request.FILES)
    
    
    return render (request, 'AppsProyecto/inicio.html',{"form":form,"posts":posts,"url":obtenerAvatar(request)})


def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user.id)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen=""
    return imagen
    

#------------------------------------------------------------------------------------
@login_required
def insertPost(request):
    posts = Post.objects.filter(state=True)
    
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'AppsProyecto/inicio.html',{"mensaje": "Post cargado!"})   
    context = {'form':form,'posts':posts}
    return render (request, 'AppsProyecto/publicar.html',context)
    


def post(request, pk):
	post = Post.objects.get(id=pk)
    
	
	return render(request, 'AppsProyecto/post.html',{"post":post})

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

@login_required
def eliminarpost(request, pk):
    post =  Post.objects.get(id=pk)
    post.delete()
    return render(request, 'AppsProyecto/inicio.html')
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
    return render(request, 'AppsProyecto/perfil.html', {'form':form, 'usuario':usuario})


def agregarAvatar(request):
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)>0):
                avatarViejo.delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'AppsProyecto/inicio.html', {'usuario':request.user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE', "imagen":obtenerAvatar(request)})
    else:
        formulario=AvatarForm()
    return render(request, 'AppsProyecto/agregaravatar.html', {'form':formulario, 'usuario':request.user, "imagen":obtenerAvatar(request)})




