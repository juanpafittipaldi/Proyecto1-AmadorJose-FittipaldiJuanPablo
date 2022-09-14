import django_filters
from .models import * 

class PedidoFiltro(django_filters.FilterSet):
    class Meta: 
        model = Pedido
        fields = '__all__' 
        exclude = ['cliente', 'fecha_creacion']