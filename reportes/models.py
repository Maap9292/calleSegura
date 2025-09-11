from django.db import models
from django.contrib.auth.models import User

class reporte(models.Model):

    titulo_reporte = models.CharField(max_length=200)
    descripcion_reporte = models.CharField(max_length=500)

    #direccion preparada para geolocalización
    direccion = models.CharField(max_length=250, blank=True, null=True) 
    latitud = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)

    fecha_reporte = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado_reporte = models.CharField(
        max_length=20,
        choices = [
            ('pendiente', 'Pendiente'),
            ('en_progreso', 'En progreso'), 
            ('reparado', 'Reparado')
            ],
        default='pendiente'
    )

    def __str__(self):
        return self.titulo_reporte