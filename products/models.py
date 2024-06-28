from django.db import models

class Product(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    data_adicionado = models.DateTimeField(auto_now_add=True)
    fornecedor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
