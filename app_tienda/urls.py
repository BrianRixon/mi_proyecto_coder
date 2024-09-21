from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name='inicio'),
    path('productos',productos, name='productos'),
    path('usuarios',usuarios, name='usuarios'),
    path('turnos', turnos, name='turnos'),
    path('registro',registro, name='registro')    
]
