from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'resto/panel.html')

def productos(request):
    return render(request, 'resto/productos.html')

def cliente(request):
    return render(request, 'resto/cliente.html')    

