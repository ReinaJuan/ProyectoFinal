from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('usuario/', users, name= 'usuario'),
    path('noticias/', notis, name= 'noticias'),
    path('deportes/', deportes , name= 'deportes'),
    path('espectaculo/', espectaculo , name= 'espectaculo'),
    path('clima/', clima , name= 'clima'),
    
    path('busquedausuario/', busquedausuario, name='busquedausuario'),
    path('buscar/', buscar, name='buscar'),
    path('', inicio, name='inicio'),

    path ('publicar/',insertPost ,name='insertUrl'),
    path('post/<str:pk>/', post, name="post"),
    path ('edit/<str:pk>',editPost ,name='editUrl'),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='AppsProyecto/logout.html'), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    
    
    
   

]