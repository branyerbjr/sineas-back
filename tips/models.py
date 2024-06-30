from django.db import models
from products.models import Product
from iot.models import Dispositivo


class InitialConfig(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    paso = models.PositiveIntegerField()
    contenido = models.TextField()

    class Meta:
        ordering = ['paso']

    def __str__(self):
        return f"Configuración inicial para {self.product}"


class UsabilityTutorials(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    imagen_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Tutorial de usabilidad para {self.product}"


class UsageTips(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()

    def __str__(self):
        return f"Consejo de uso para {self.product}"


class Maintenance(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()

    def __str__(self):
        return f"Mantenimiento para {self.product}"


class Support(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()

    def __str__(self):
        return f"Soporte para {self.product}"
