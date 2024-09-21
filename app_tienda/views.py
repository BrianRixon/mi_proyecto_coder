from django.shortcuts import render
from .models import Registro
from django.http import HttpResponse
# Create your views here.

def crear_usuario(req, nombre, apellido, documento, email):
    nuevo_usuario= Registro(nombre=nombre, apellido=apellido, documento=documento, email=email)
    nuevo_usuario.save()

    return HttpResponse(f'<p>el usuario {nuevo_usuario.nombre}{nuevo_usuario.apellido} fue creado con exito!</p>')





















# render templates
def inicio(req):

    return render(req, "base.html",{})

def productos(req):
    
    return render(req, "productos.html", {})

def usuarios(req):
    return render(req, "usuarios.html",{})

def turnos(req):
    return render(req, "turnos.html",{})

def registro(req):
    return render(req, "registro.html",{})
