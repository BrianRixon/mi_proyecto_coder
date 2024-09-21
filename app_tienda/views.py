from django.shortcuts import render

# Create your views here.

def inicio(req):

    return render(req, "base.html",{})

def productos(req):
    
    return render(req, "productos.html", {})

def usuarios(req):
    return render(req, "usuarios.html",{})
