from django.db import models
from iot.models import Hogar, Dispositivo


class Rules(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    hogar = models.ForeignKey(Hogar, on_delete=models.CASCADE)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    condicion = models.CharField(max_length=255)
    accion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Shadow(models.Model):
    dispositivo = models.OneToOneField(Dispositivo, on_delete=models.CASCADE)
    estado = models.JSONField()

    def __str__(self):
        return f'Shadow de {self.dispositivo.nombre}'


class RelaySchedule(models.Model):
    MESSAGE_CHOICES = [
        ('on', 'On'),
        ('off', 'Off'),
    ]

    message = models.CharField(max_length=3, choices=MESSAGE_CHOICES)
    time = models.TimeField()
    hogar = models.ForeignKey(Hogar, on_delete=models.CASCADE)  # Relación con el hogar
    last_state = models.CharField(max_length=3, choices=MESSAGE_CHOICES, null=True, blank=True)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)  # Relación con el dispositivo

    def __str__(self):
        return f"Message: {self.get_message_display()}, Time: {self.time}, Hogar: {self.hogar.nombre}, Dispositivo: {self.dispositivo.nombre}"