from __future__ import unicode_literals

from django.db import models

class UnidadAcademica(models.Model):

	nombre = models.CharField(max_length=100)
	url = models.CharField(max_length=100)
