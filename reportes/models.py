from django.conf import settings
from django.db import models
from ubicaciones.models import Ciudad
from ciudadanos.models import Ciudadano
##from django.contrib.auth.models import User

class Reporte(models.Model):

    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('reparado', 'Reparado'),
    ]

    titulo_reporte = models.CharField(max_length=200)
    descripcion_reporte = models.CharField(max_length=500)

    #direccion preparada para geolocalización
    direccion = models.CharField(max_length=250, blank=True, null=True) 
    latitud = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=7, null=True, blank=True)

    fecha_reporte = models.DateTimeField(auto_now_add=True)
    ciudadano = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='reportes')
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True, blank=True)
    entidad_responsable = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="reportes_asignados")

    estado_reporte = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")

    imagen = models.ImageField(upload_to='reportes/', null=True, blank=True)

    class Meta:
        permissions = [
            ('can_change_status', 'Can change report status'),
        ]

    def __str__(self):
        return self.titulo_reporte