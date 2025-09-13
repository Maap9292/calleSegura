from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Reporte

User = get_user_model()


class ReporteSerializer(serializers.ModelSerializer):

    ciudadano = serializers.PrimaryKeyRelatedField(read_only=True)
    ciudadano_info = serializers.SerializerMethodField(read_only=True)
    entidad_responsable = serializers.PrimaryKeyRelatedField(read_only=True)
    entidad_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Reporte
        fields = [
            'id', 'titulo_reporte', 'descripcion_reporte',
            'direccion', 'latitud', 'longitud',
            'fecha_reporte', 'ciudad', 'ciudadano', 'ciudadano_info',
            'entidad_responsable', 'entidad_info', 'estado_reporte'
        ]
    
    def get_ciudadano_info(self, obj):
        if obj.ciudadano:
            return {'id': obj.ciudadano.id, 'username': obj.ciudadano.username}
        return None
    
    def get_entidad_info(self, obj):
        if obj.entidad_responsable:
            return {'id': obj.entidad_responsable.id, 'username': obj.entidad_responsable.username}
        return None
