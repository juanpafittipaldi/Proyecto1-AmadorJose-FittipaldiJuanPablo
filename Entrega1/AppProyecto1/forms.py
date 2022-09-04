from socket import fromshare
from django import forms

class ClienteForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    edad= forms.IntegerField()
    mail= forms.EmailField()

class MozoForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    edad= forms.IntegerField()
    sector=forms.CharField()

class PlatoForm(forms.Form):
    categoria= forms.CharField(max_length=50)
    nombre_plato= forms.CharField(max_length=50)
    precio=forms.IntegerField()
