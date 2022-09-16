from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
#Esta importación faltaba y por eso no aparecía PedidoForm (y luego el ClienteForm) como undefined. 
from .formularios import PedidoForm, ClienteForm, ProductoForm
#Para filtrar los pedidos en la vista del cliente
from .filtros import PedidoFiltro
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
    
    #Para filtrar 
    filtro = PedidoFiltro(request.GET, queryset=pedidos)
    pedidos = filtro.qs

    #Se agrega el contexto
    context = {'cliente':cliente, 'pedidos':pedidos, 'pedidos_contador':pedidos_contador, 'filtro':filtro}
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


def crearPedido(request):
	form = PedidoForm()
	if request.method == 'POST':
		form = PedidoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
 
	context = {'form':form}
	return render(request, 'resto/formulario_pedido.html', context)

def crearProducto(request):
	form = ProductoForm()
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
 
	context = {'form':form}
	return render(request, 'resto/formulario_producto.html', context)


def actualizarPedido(request, pk): 
	pedido = Pedido.objects.get(id=pk)
	form = PedidoForm(instance=pedido)
	
	if request.method == 'POST': 
		form = PedidoForm(request.POST, instance=pedido)
		if form.is_valid():
			form.save()
			return redirect('/')
		

	context = {'form':form}
	return render(request, 'resto/formulario_pedido.html', context)


def eliminarPedido(request, pk): 
	pedido = Pedido.objects.get(id=pk)
	if request.method == 'POST': 
			pedido.delete()
			return redirect('/')
	context = {'item':pedido}
	return render(request, 'resto/eliminar_pedido.html', context)
