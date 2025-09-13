from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Reporte
from .serializers import ReporteSerializer
from .permissions import IsEntidad

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all().order_by('-fecha_reporte')
    serializer_class = ReporteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # GET público, POST requiere auth

    def perform_create(self, serializer):
        # asigna automáticamente el usuario autenticado como ciudadano creador
        serializer.save(ciudadano=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsEntidad])
    def cambiar_estado(self, request, pk=None):
        reporte = self.get_object()
        nuevo_estado = request.data.get('estado_reporte')
        if nuevo_estado not in dict(Reporte.ESTADOS):
            return Response({'detail': 'Estado inválido.'}, status=status.HTTP_400_BAD_REQUEST)
        reporte.estado_reporte = nuevo_estado
        reporte.entidad_responsable = request.user
        reporte.save()
        return Response(self.get_serializer(reporte).data)


