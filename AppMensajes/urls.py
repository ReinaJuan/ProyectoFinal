from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    
    path('mensaje/', mensaje, name='mensaje'),
    path('bandejaentrada/', bandejaaentrada, name='bandejaentrada'),
    path('bandejasalida/', bandejasalida, name='bandejasalida'),
    path('logout/', LogoutView.as_view(template_name='AppMensajes/logout.html'), name='logout')
    
    
    
    
   

]