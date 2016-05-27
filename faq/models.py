from django.db import models

class FuentesJSON(models.Model):
	nombre = models.CharField(max_length = 20)
	descripcion = models.CharField(max_length = 100)
	fuente = models.CharField(max_length = 100)

	def __str__(self):
		return self.nombre
