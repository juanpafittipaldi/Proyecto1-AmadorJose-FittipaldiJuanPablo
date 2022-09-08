from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('productos/', views.productos),
    path('cliente/', views.cliente),
    path('crear_pedido/', views.crearPedido, name="crear_pedido"),
]
