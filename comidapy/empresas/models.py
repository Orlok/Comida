from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Empresa(models.Model):
	nombre = models.CharField( max_length=20, unique=True)
	descripcion = models.CharField (max_length = 300)
	createdby = models.ForeignKey(User)
	createdat = models.DateTimeField(auto_now_add=True)

	# createdat = models.DateTimeField(auto_now_add=True)
	# foto = models.ImageField()