from django.db import models

class Ciudad(models.Model):

    nombre = models.CharField(max_length=200, unique=True)
    distrito = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre