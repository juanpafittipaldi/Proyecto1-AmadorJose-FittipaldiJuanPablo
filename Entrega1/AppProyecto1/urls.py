from django.urls import path
from AppProyecto1.views import *

urlpatterns = [
    path('felicitaciones/', felicitaciones),
    path('clienteformulario/', clienteformulario, name="clienteformulario"),

]
