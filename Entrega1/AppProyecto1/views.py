from django.shortcuts import render
from AppProyecto1.forms import ClienteForm
from AppProyecto1.models import *
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