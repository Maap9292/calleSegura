from django.db import models
from django.contrib.auth.models import AbstractUser

class Ciudadano(AbstractUser):

    ROLE_CHOICES = [
        ('ciudadano', 'Ciudadano'),
        ('entidad', 'Entidad Gubernamental'),
        ('admin', 'Administrador'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='ciudadano')

    telefono = models.CharField(max_length=20, blank=True, null=True)
    ubicacion = models.CharField(
        max_length=100,
        choices = [
            ('santa ana centro', 'Santa Ana Centro'),
            ('santa ana oeste', 'Santa Ana Oeste')
        ],
        blank=True, null=True
    )
    direccion = models.CharField(max_length=200, blank=True, null=True)
    #email = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if self.groups.filter(name="Entidad").exists():
            return f"{self.username} (Entidad)"
        return f"{self.username} (Ciudadano)"
