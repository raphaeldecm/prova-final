from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome