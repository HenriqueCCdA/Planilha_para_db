from django.db import models


class Tabela(models.Model):

    nome = models.CharField(max_length=200)
    saldo = models.IntegerField()
