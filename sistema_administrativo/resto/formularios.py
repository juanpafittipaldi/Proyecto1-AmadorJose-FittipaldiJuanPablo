from django.forms import ModelForm
from .models import *


class PedidoForm(ModelForm):
	class Meta:
		model = Pedido
		fields = '__all__'

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente
		fields = '__all__'

class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		fields = '__all__'