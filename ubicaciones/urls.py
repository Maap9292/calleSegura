from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CiudadViewSet

router = DefaultRouter()
router.register(r'ciudades', CiudadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
