from django.shortcuts import render
from django.shortcuts import redirect
from .models import Registro, Productos
from django.http import HttpResponse
from .forms import RegistroFormulario
# Create your views here.

#crea un nuevo registro en DB
def form_de_registro(request):
    if request.method == 'POST':

        nuevo_formulario = RegistroFormulario(request.POST)

        if nuevo_formulario.is_valid():
            data= nuevo_formulario.cleaned_data

            nuevo_usuario= Registro(nombre=data["nombre"],
                                    apellido=data["apellido"],
                                    documento=data["documento"],
                                    email=data["email"])
            nuevo_usuario.save()

            return render(request,'registro_exitoso.html')
        
        else:
            return render(request, 'registro.html', {'nuevo_formulario': nuevo_formulario})
        
    else:
        mi_formulario = RegistroFormulario()

        return render(request, 'registro.html', {'mi_formulario': mi_formulario})


# busca usuario
def buscar_usuario(request):

     busqueda = request.GET["nombre"]

     resultados = Registro.objects.filter(nombre__icontains=busqueda)

    
     return render(request, "buscar_usuario.html", {"resultados": resultados})
 








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


def registro_exitoso(req):
    return render(req, "registro_exitoso.html",{})

