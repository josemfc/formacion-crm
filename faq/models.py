from django.db import models
from formacion.ftp import FTPStorage
from django.conf import settings


fs = FTPStorage()

def upload_path_handler(instance, filename):    # Indica dónde subir archivo
    return "{f}".format(f=filename)

class FuentesJSON(models.Model):
	nombre = models.CharField(max_length = 20)
	descripcion = models.CharField(max_length = 100)
	fuente = models.FileField('Fuente de datos', upload_to = upload_path_handler, storage = fs)
	
	def _get_filename_fuente(self):
		return settings.MEDIA_ROOT + self.fuente.name
    
	filename_fuente = property(_get_filename_fuente)

	def __str__(self):
		return self.nombre
