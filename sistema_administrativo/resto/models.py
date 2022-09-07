from django.db import models

# Create your models here.


class Cliente(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Producto(models.Model):
	CATEGORY = (
			('Apto Vegano', 'Apto Vegano'),
			('No apto Vegano', 'No apto Vegano'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Pedido(models.Model):
	STATUS = (
			('Pendiente', 'Pendiente'),
			('En camino', 'En camino'),
			('Entregado', 'Entregado'),
			)

	cliente = models.ForeignKey(Cliente, null=True, on_delete= models.SET_NULL)
	producto = models.ForeignKey(Producto, null=True, on_delete= models.SET_NULL)
	fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)