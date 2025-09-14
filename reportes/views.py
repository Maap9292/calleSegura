from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Reporte
from .serializers import ReporteSerializer
from .permissions import EsCiudadano, EsEntidad

class ReporteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para Reporte:
    - GET: público
    - POST: solo Ciudadanos
    - PATCH/PUT: solo Entidades
    - DELETE: solo Entidades si se necesita
    """
    queryset = Reporte.objects.all().order_by('-fecha_reporte')
    serializer_class = ReporteSerializer

    def get_permissions(self):
        """
        Define permisos según la acción:
        - Crear (POST) → Ciudadanos
        - Actualizar/Parcial (PUT/PATCH) → Entidades
        - Cambiar estado (acción personalizada) → Entidades
        - Listar/Detalle (GET) → Público
        """
        if self.action == "create":
            permission_classes = [permissions.IsAuthenticated, EsCiudadano]
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [permissions.IsAuthenticated, EsEntidad]
        elif self.action == "cambiar_estado":
            permission_classes = [permissions.IsAuthenticated, EsEntidad]
        else:
            permission_classes = [permissions.AllowAny]  # GET público
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """
        Asigna automáticamente el usuario autenticado como ciudadano creador.
        """
        serializer.save(ciudadano=self.request.user)

    @action(
        detail=True,
        methods=['post'],
        permission_classes=[permissions.IsAuthenticated, EsEntidad]  # Solo entidades
    )
    def cambiar_estado(self, request, pk=None):
        """
        Acción personalizada para que las entidades cambien el estado del reporte.
        """
        reporte = self.get_object()
        nuevo_estado = request.data.get('estado_reporte')

        if nuevo_estado not in dict(Reporte.ESTADOS):
            return Response(
                {'detail': 'Estado inválido.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Actualiza estado y asigna la entidad responsable
        reporte.estado_reporte = nuevo_estado
        reporte.entidad_responsable = request.user
        reporte.save()

        return Response(self.get_serializer(reporte).data)



