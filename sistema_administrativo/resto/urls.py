from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('productos/', views.productos, name="productos"),
    path('cliente/<str:pk_cliente>/', views.cliente, name="cliente"),
    path('crear_pedido/', views.crearPedido, name="crear_pedido"),
    path('crear_cliente/', views.crearCliente, name="crear_cliente"),
    path('crear_producto/', views.crearProducto, name="crear_producto"), 
    #Actualizar Pedido
    path('actualizar_pedido/<str:pk>', views.actualizarPedido, name="actualizar_pedido"),
]



