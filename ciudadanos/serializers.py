from rest_framework import serializers
from .models import Ciudadano

class CiudadanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudadano
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'telefono', 'ubicacion', 'direccion', 'role']

        read_only_fields = ['id']

