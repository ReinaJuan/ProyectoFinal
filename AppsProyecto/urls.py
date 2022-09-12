from django.urls import path
from .views import *

urlpatterns = [
    path('usuario/', users, name= 'usuario'),
    path('noticias/', notis, name= 'noticias'),
    path('deportes/', deportes , name= 'deportes'),
    path('espectaculo/', espectaculo , name= 'espectaculo'),
    path('clima/', clima , name= 'clima'),
    path('', inicio , name= 'inicio'),
    path('busquedausuario/', busquedausuario, name='busquedausuario'),
    path('buscar/', buscar, name='buscar'),
    
    
    
   

]