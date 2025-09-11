from django.shortcuts import render
from rest_framework import viewsets
from .models import reporte
from .serializers import reporteSerializer


#Para crear operaciones GET, POST, DELETE y PUT en el modelo
class reporteViewSet(viewsets.ModelViewSet):

    queryset = reporte.objects.all()
    serializer_class = reporteSerializer

