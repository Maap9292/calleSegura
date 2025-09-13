from rest_framework.permissions import BasePermission

class IsEntidad(BasePermission):
    """
    Permite la acción solo a usuarios autenticados con role == 'entidad' o staff.
    """
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and (getattr(user, 'role', '') == 'entidad' or user.is_staff))
