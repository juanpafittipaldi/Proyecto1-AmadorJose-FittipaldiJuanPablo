from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
#Esta importación faltaba y por eso no aparecía PedidoForm como undefined. 
from .formularios import PedidoForm, ClienteForm
# Create your views here.
def home(request):
    pedidos = Pedido.objects.all()
    clientes = Cliente.objects.all()
    total_clientes = clientes.count()
    total_pedidos = pedidos.count()
    entregado = pedidos.filter(status='Entregado').count()
    pendiente = pedidos.filter(status='Pendiente').count()

    context= {'pedidos':pedidos, 
    'clientes':clientes, 'total_pedidos':total_pedidos, 'entregado':entregado, 'pendiente':pendiente}

    return render(request, 'resto/panel.html', context)

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'resto/productos.html', {'lista' :productos})

def cliente(request, pk_cliente):
    #Con esto entonces se puede encadenar el str al id del cliente 
    cliente = Cliente.objects.get(id=pk_cliente) 
    #Data de los pedidos al perfil del cliente 
    pedidos = cliente.pedido_set.all()
    pedidos_contador = pedidos.count()
    context = {'cliente':cliente, 'pedidos':pedidos, 'pedidos_contador':pedidos_contador}
    #Se agrega el contexto
    return render(request, 'resto/cliente.html', context)    

def crearPedido(request):
	form = PedidoForm()
	if request.method == 'POST':
		form = PedidoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
 
	context = {'form':form}
	return render(request, 'resto/formulario_pedido.html', context)


def crearCliente(request):
	form = ClienteForm()
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
 
	context = {'form':form}
	return render(request, 'resto/formulario_cliente.html', context)