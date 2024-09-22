from django.shortcuts import render
from .models import Registro
from django.http import HttpResponse
from .forms import RegistroFormulario
# Create your views here.


# def form_de_registro(req):
#     if req.method == 'POST':
        
#         mi_formulario = RegistroFormulario(req.POST)
#         mi_formulario.save()

#         print(mi_formulario)

#         return render(req,'inicio.html')
    
#     else:
#         mi_formulario = RegistroFormulario()

#         return render(req,'registro.html', {"mi_formulario": mi_formulario})
    


def form_de_registro(request):
    if request.method == 'POST':
        nuevo_formulario = RegistroFormulario(request.POST)
        if nuevo_formulario.is_valid():
            
            nombre = nuevo_formulario.cleaned_data['nombre']
            apellido = nuevo_formulario.cleaned_data['apellido']
            documento = nuevo_formulario.cleaned_data['documento']
            email = nuevo_formulario.cleaned_data['email']

            Registro.objects.create(
                nombre=nombre,
                apellido=apellido,
                documento=documento,
                email=email
            )
        return render(request, 'base.html',{})
            
    else:
        nuevo_formulario = RegistroFormulario()

    return render(request, 'registro.html', {'nuevo_formulario': nuevo_formulario})

























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
