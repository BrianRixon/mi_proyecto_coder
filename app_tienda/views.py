from django.shortcuts import render
from django.shortcuts import redirect
from .models import Registro, Productos
from django.http import HttpResponse
from .forms import RegistroFormulario
# Create your views here.


def form_de_registro(request):
    if request.method == 'POST':

        nuevo_formulario = RegistroFormulario(request.POST)

        if nuevo_formulario.is_valid():
            data= nuevo_formulario.cleaned_data

            nuevo_usuario= Registro(nombre=data["nombre"], apellido=data["apellido"], documento=data["documento"], email=data["email"])
            nuevo_usuario.save()

            # Redirigir después de la creación exitosa
            return render(request,'registro_nuevo.html')
        
    else:
        nuevo_formulario = RegistroFormulario()

    return render(request, 'registro.html', {'nuevo_formulario': nuevo_formulario})




# def buscar_producto(request):
   
#    if request.GET["producto"]:
       
#     producto= request.GET['producto']
#     busqueda= Productos.objects.filter(producto__icontains = producto)

#     return render(request, 'resultado_busqueda.html',{"producto":busqueda})
   
def buscar_producto(request):
    producto = request.GET.get("producto", "")
    
    if producto:
        busqueda = Productos.objects.filter(producto__icontains=producto)
    else:
        busqueda = Productos.objects.none()  # Devuelve una queryset vacía si no hay producto

    return render(request, 'buscar_producto.html', {"producto": busqueda})








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

def buscar_producto(req):
    return render(req, "buscar_producto.html",{})

def registro_nuevo(req):
    return render(req, "registro_nuevo.html",{})