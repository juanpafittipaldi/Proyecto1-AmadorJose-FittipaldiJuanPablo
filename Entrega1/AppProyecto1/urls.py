from django.urls import path
from AppProyecto1.views import *

urlpatterns = [
    path('felicitaciones/', felicitaciones),
    path('clienteformulario/', clienteformulario, name="clienteformulario"),
    path('mozoformulario/', mozoformulario, name="mozoformulario"),
    path('platoformulario/', platoformulario, name="platoformulario"),
    path('busquedacliente/', busquedacliente, name="busquedacliente"),
    path('busquedamozo/', busquedamozo, name="busquedamozo"),
    path('busquedaplato/', busquedaplato, name="busquedaplato"),
    path('resultadobusquedacliente/', resultadobusquedacliente, name="resultadobusquedacliente"),
    path('',index,name="index")
]
