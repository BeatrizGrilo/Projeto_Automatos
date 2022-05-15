from django.db import models

# Create your models here.

class Automato(models.Model):
    descricao = models.CharField(max_length=1000)
    alfabeto = models.CharField(max_length=200)
    estados = models.CharField(max_length=200)
    estadoinicial = models.CharField(max_length=200)
    estadodeaceitacao = models.CharField(max_length=200)
    transicoes = models.CharField(max_length=8000)

    def __str__(self):
        return self.descricao[:50]


class MaquinaTuring(models.Model):
    descricao = models.CharField(max_length=1000)
    estados = models.CharField(max_length=200)
    estadoinicial = models.CharField(max_length=200)
    estadodeaceitacao = models.CharField(max_length=200)
    transicoes = models.CharField(max_length=8000)

    def __str__(self):
        return self.descricao[:50]
