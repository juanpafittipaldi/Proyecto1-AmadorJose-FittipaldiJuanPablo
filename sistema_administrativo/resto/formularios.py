from django.formularios import ModelForm
from .models import Pedido


class PedidoForm(ModelForm):
	class Meta:
		model = Pedido
		fields = '__all__'