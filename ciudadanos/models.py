from django.db import models
from django.contrib.auth.models import AbstractUser

class ciudadano(AbstractUser):

    telefono = models.CharField(max_length=20, blank=True, null=True)
    ubicacion = models.CharField(
        choices = [
            ('santa ana centro', 'Santa Ana Centro'),
            ('santa ana oeste', 'Santa Ana Oeste')
        ]
    )
    direccion = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

def __str__(self):
    return f"{self.username} (ciudadano)"
