from django.shortcuts import render
from rest_framework import viewsets
from .models import Ciudadano
from .serializers import CiudadanoSerializer

class CiudadanoViewSet(viewsets.ModelViewSet):
    queryset = Ciudadano.objects.all()
    serializer_class = CiudadanoSerializer

