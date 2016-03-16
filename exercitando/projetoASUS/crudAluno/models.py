from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pessoa(models.Model):
	primeiro_nome = models.CharField(max_length=30, blank=False)
	ultimo_nome = models.CharField(max_length=30)
	email = models.EmailField(unique=True)
	idade = models.IntegerField()
	genero = models.CharField(max_length=100, blank=False)

	periodo = models.IntegerField()
	cra = models.DecimalField(max_digits=4, decimal_places=2)
	curso = models.CharField(max_length=30, blank=False)

	def __str__(self):
		return self.primeiro_nome