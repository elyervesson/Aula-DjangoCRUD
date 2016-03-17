from __future__ import unicode_literals

from django.db import models
from random import randint

# Create your models here.
class Aluno(models.Model):
	primeiro_nome = models.CharField(max_length=30)
	ultimo_nome = models.CharField(max_length=30)
	email = models.EmailField()

	idade = models.IntegerField()
	genero = models.CharField(max_length=100, blank=False)

	periodo = models.IntegerField()
	cra = models.DecimalField(max_digits=4, decimal_places=2)
	curso = models.CharField(max_length=30, blank=False)

	matricula = str(randint(1000000,9999999))

	def __str__(self):
		return self.primeiro_nome