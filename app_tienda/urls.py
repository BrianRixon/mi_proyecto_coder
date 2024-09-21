from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio),
    path('productos',productos, name='productos'),
    path('usuarios',usuarios, name='usuarios')    
]
