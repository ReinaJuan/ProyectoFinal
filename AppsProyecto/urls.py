from django.urls import path
from .views import *
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('busquedausuario/', busquedausuario, name='busquedausuario'),
    path('buscar/', buscar, name='buscar'),
    path('', inicio, name='inicio'),

    path ('publicar/',insertPost ,name='insertUrl'),
    path('post/<str:pk>/', post, name="post"),
    path ('edit/<str:pk>',editPost ,name='editUrl'),
    path('delete/<str:pk>',eliminarpost ,name='deleteUrl'),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='AppsProyecto/logout.html'), name='logout'),
    path('perfil/', editarPerfil, name='perfil'),
    path('agregaravatar/', agregarAvatar,name='agregaravatar'),
    path('acercadenosotros/', acercadenosotros,name='acercadenosotros'),
    
    
    
   

]