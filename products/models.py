from django.db import models
from django.utils import timezone
from customers.models import CustomUser
import uuid


class Product(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    data_adicionado = models.DateTimeField(auto_now_add=True)
    fornecedor = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, unique=True)
    codigo_vendido = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    es_iot = models.BooleanField(default=False)
    galeria_imagenes = models.TextField(blank=True, help_text="Ingrese URLs de imágenes separadas por comas")

    def __str__(self):
        return self.nome


class Purchase(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchase_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.customer.email} - {self.product.nome}'

    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'
