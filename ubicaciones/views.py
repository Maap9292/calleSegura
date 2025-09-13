from django.shortcuts import render
from rest_framework import viewsets
from .models import Ciudad
from .serializers import CiudadSerializer

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
