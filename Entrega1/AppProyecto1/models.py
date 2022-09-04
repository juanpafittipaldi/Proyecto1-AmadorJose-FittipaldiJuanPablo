from django.db import models

# Create your models here.

class mozo(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()
    sector=models.CharField(max_length=50)

class cliente(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()
    mail= models.EmailField()

class plato(models.Model):
    categoria= models.CharField(max_length=50)
    nombre_plato= models.CharField(max_length=50)
    precio=models.IntegerField()
