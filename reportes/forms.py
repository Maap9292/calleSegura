# reportes/forms.py
from django import forms
from .models import Reporte

class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = [
            'titulo_reporte',
            'descripcion_reporte',
            'direccion',
            'latitud',
            'longitud',
            'ciudad',  # si quieres que el usuario seleccione la ciudad
            'imagen',
        ]

class CambiarEstadoForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['estado_reporte']




