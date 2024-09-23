from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name='inicio'),
    path('productos',productos, name='productos'),
    path('usuarios',usuarios, name='usuarios'),
    path('turnos', turnos, name='turnos'),
    path('registro', registro, name='registro'),
    path('formulario_registro', form_de_registro, name='RegistroFormulario' ),
    path('buscar_usuario', buscar_usuario, name='buscar_usuario'),
    path('registro_exitoso', registro_exitoso, name='registro_exitoso')    
]
