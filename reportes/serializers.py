from rest_framework import serializers
from .models import reporte

class reporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = reporte
        fields = '__all__'  # O lista de campos que quieras exponer
