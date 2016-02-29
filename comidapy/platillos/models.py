from __future__ import unicode_literals

from django.db import models
from empresas.models import Empresa

# Create your models here.
class Platillo(models.Model):
	nombre = models.CharField( max_length=20, unique=True)
	descripcion = models.CharField (max_length = 300)
	# foto = models.ImageField()
	precio = models.DecimalField(default=0.0, decimal_places=2, max_digits = 9)
	vigencia = models.DateField(auto_now=False)
	empresa = models.ForeignKey(Empresa)
