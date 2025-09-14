from rest_framework import permissions

class EsCiudadano(permissions.BasePermission):
    """
    Permite solo crear reportes si es Ciudadano.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and not request.user.groups.filter(name="Entidad").exists()


class EsEntidad(permissions.BasePermission):
    """
    Permite solo editar el estado si es Entidad.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name="Entidad").exists()


