from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
# Create your views here.
def home(request):
    return render(request, 'resto/panel.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'resto/productos.html', {'lista' :productos})

def cliente(request):
    return render(request, 'resto/cliente.html')    

