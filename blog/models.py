from django.db import models
from django.utils import timezone #from->se emplea para agregar/importar cosas que son de otros archivos

class Post(models.Model):#Acá se define el modelo class->indica que se está definiendo un objeto, Post->nombre del modelo, models.Model->significa que Post es un modelo de django

##Ahora se definen las propiedades de autor, titullo, texto...
	author=models.ForeignKey('auth.User')#Relación con otro modelo
	title= models.CharField(max_length=200) ##con esto es para crear un texto largo
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)##Definir fecha y hora
	published_date=models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def _str_(self):
		return self.title #Esta funcion retorna el titulo
	
