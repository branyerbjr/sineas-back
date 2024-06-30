from django.db import models
from django.core.exceptions import ValidationError
from customers.models import CustomUser
from products.models import Product
import uuid


class Hogar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    propietario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timezone = models.CharField(max_length=100, default='UTC')

    def __str__(self):
        return self.nombre


class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    hogar = models.ForeignKey(Hogar, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.topic:
            self.topic = f'{self.hogar.nombre.lower()}_{uuid.uuid4().hex[:8]}'
        super().save(*args, **kwargs)

    def clean(self):
        if not self.product.es_iot:
            raise ValidationError(f"El producto '{self.product.nome}' no es un dispositivo IoT.")

    def __str__(self):
        return self.nombre
