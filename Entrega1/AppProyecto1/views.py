from django.shortcuts import render
from AppProyecto1.forms import *
from AppProyecto1.models import *
from django.http import HttpResponse
# Create your views here.
def felicitaciones(request):
    return render(request,"AppProyecto1/felicitaciones.html")

def clienteformulario(request):
    if request.method=="POST":
        form=ClienteForm(request.POST)
        print("--------------------")
        print(form)
        print("--------------------")
        if form.is_valid():
            
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            edad=informacion["edad"]
            mail=informacion["mail"]
            cli=cliente(nombre=nombre,apellido=apellido,edad=edad,mail=mail)
            cli.save()
            return render(request,"AppProyecto1/felicitaciones.html")

    else:
        formulario=ClienteForm()
        return render(request, "AppProyecto1/clienteformulario.html", {"formulario":formulario})

def mozoformulario(request):
    if request.method=="POST":
        form=MozoForm(request.POST)
        print("--------------------")
        print(form)
        print("--------------------")
        if form.is_valid():
            
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            edad=informacion["edad"]
            sector=informacion["sector"]
            moz=mozo(nombre=nombre,apellido=apellido,edad=edad,sector=sector)
            moz.save()
            return render(request,"AppProyecto1/felicitaciones.html")

    else:
        formulario=MozoForm()
        return render(request, "AppProyecto1/mozoformulario.html", {"formulario":formulario})

def platoformulario(request):
    if request.method=="POST":
        form=PlatoForm(request.POST)
        print("--------------------")
        print(form)
        print("--------------------")
        if form.is_valid():
            
            informacion=form.cleaned_data
            print(informacion)
            categoria=informacion["categoria"]
            nombre_plato=informacion["nombre_plato"]
            precio=informacion["precio"]
            plat=plato(categoria=categoria,nombre_plato=nombre_plato,precio=precio)
            plat.save()
            return render(request,"AppProyecto1/felicitaciones.html")

    else:
        formulario=PlatoForm()
        return render(request, "AppProyecto1/platoformulario.html", {"formulario":formulario})

def busquedacliente(request):
    return render(request,"AppProyecto1/busquedacliente.html")

def resultadobusquedacliente(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        clientes=cliente.objects.filter(nombre=nombre)
        return render(request,"AppProyecto1/resultadobusquedacliente.html",{"clientes":clientes})
    else:
        return render(request,"AppProyecto1/busquedacliente.html", {"mensaje":"Ingresa un nombre de cliente"})

def busquedamozo(request):
    return render(request,"AppProyecto1/busquedamozo.html")

def busquedaplato(request):
    return render(request,"AppProyecto1/busquedaplato.html")

def index(request):
    return render(request,"AppProyecto1/index.html")